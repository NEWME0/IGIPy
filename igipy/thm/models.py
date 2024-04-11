import json
import struct
from array import array
from itertools import islice
from pathlib import Path
from typing import BinaryIO, Self

from PIL import Image
from pydantic import BaseModel, ValidationError

from igipy.utils import BinaryFormat


class EmptyStreamError(ValueError):
    pass


class ThmHeader(BaseModel):
    unknown_0: int
    creation_year: int
    creation_month: int
    creation_day: int
    creation_hour: int
    creation_minute: int
    creation_second: int
    creation_millisecond: int
    unknown_1: int
    unknown_2: int
    unknown_3: int
    width: int
    height: int

    @classmethod
    def from_stream(cls, stream: BinaryIO) -> Self:
        header_bytes = stream.read(52)

        if len(header_bytes) < 52:
            raise ValueError(
                f"Not enough bytes for headers: {len(header_bytes)}. Need 52"
            )

        (
            unknown_0,
            creation_year,
            creation_month,
            creation_day,
            creation_hour,
            creation_minute,
            creation_second,
            creation_millisecond,
            unknown_1,
            unknown_2,
            unknown_3,
            width,
            height,
        ) = struct.unpack("13I", header_bytes)

        return cls(
            unknown_0=unknown_0,
            creation_year=creation_year,
            creation_month=creation_month,
            creation_day=creation_day,
            creation_hour=creation_hour,
            creation_minute=creation_minute,
            creation_second=creation_second,
            creation_millisecond=creation_millisecond,
            unknown_1=unknown_1,
            unknown_2=unknown_2,
            unknown_3=unknown_3,
            width=width,
            height=height,
        )

    def to_dict(self) -> dict:
        return self.dict()


class ThmLod(BaseModel):
    data: bytes
    number: int
    width: int
    height: int

    @classmethod
    def from_stream(
        cls, stream: BinaryIO, width: int, height: int, lod_number: int
    ) -> Self:
        lod_width = width // (1 << lod_number)
        lod_height = height // (1 << lod_number)
        lod_length = lod_width * lod_height * 4
        lod_bytes = stream.read(lod_length)

        if len(lod_bytes) == 0:
            raise EmptyStreamError("Stream is empty")

        if len(lod_bytes) < lod_length:
            raise ValidationError("Not enough data to build a lod")

        return cls(data=lod_bytes, number=lod_number, width=lod_width, height=height)

    def to_dict(self) -> dict:
        lod_data_array = array("f")
        lod_data_array.frombytes(self.data)

        result = self.dict()
        result["data"] = [
            list(islice(iter(lod_data_array), self.width)) for _ in range(self.height)
        ]

        return result


class Thm(BinaryFormat):
    header: ThmHeader
    lods: list[ThmLod]

    @classmethod
    def from_file(cls, path: Path | str) -> Self:
        with Path(path).open(mode="rb") as stream:
            return cls.from_stream(stream)

    @classmethod
    def from_stream(cls, stream: BinaryIO) -> Self:
        header = ThmHeader.from_stream(stream)
        lods = list()

        for lod_number in range(10):
            try:
                lod = ThmLod.from_stream(
                    stream, header.width, header.height, lod_number
                )
                lods.append(lod)
            except EmptyStreamError:
                break

        return cls(header=header, lods=lods)

    def to_dict(self) -> dict:
        return {
            "header": self.header.to_dict(),
            "lods": [lod.to_dict() for lod in self.lods],
        }

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent)

    def to_tiff(self, path: Path):
        with path.open(mode="wb") as stream:
            lod = self.lods[0]
            img = Image.new(mode="F", size=(lod.width, lod.height))
            img.frombytes(lod.data)
            img.save(stream)
