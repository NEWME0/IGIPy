import struct
import wave
from enum import IntEnum
from pathlib import Path
from typing import BinaryIO, Self

from pydantic import BaseModel, ValidationError


from igipy.utils import BinaryFormat


class SoundPackMethod(IntEnum):
    SOUND_PACK_METHOD_RAW = 0
    SOUND_PACK_METHOD_RAW_RESIDENT = 1
    SOUND_PACK_METHOD_ADPCM = 2
    SOUND_PACK_METHOD_ADPCM_RESIDENT = 3


class WavHeader(BaseModel):
    signature: bytes
    sound_pack_method: SoundPackMethod
    sample_width: int
    channels_count: int
    unknown_04: int
    frame_rate: int
    frame_count: int

    @classmethod
    def from_stream(cls, stream: BinaryIO) -> Self:
        header_bytes = stream.read(20)

        if len(header_bytes) < 20:
            raise ValidationError("Not enough bytes for header")

        (
            signature,
            sound_pack_method,
            sample_width,
            channels_count,
            unknown_04,
            frame_rate,
            frame_count,
        ) = struct.unpack('4s4H2I', header_bytes)

        if signature != b"ILSF":
            raise ValidationError(f"Unexpected signature: {signature}")

        if sound_pack_method not in (0, 1, 2, 3):
            raise ValidationError(f"Unexpected sound pack method: {sound_pack_method}")

        if sample_width != 16:
            raise ValidationError(f"Unexpected sample width: {sample_width}")

        if channels_count not in (1, 2):
            raise ValidationError(f"Unexpected channels count: {channels_count}")

        if frame_rate not in (11025, 22050, 44100):
            raise ValidationError(f"Unexpected framerate: {frame_rate}")

        return cls(
            signature=signature,
            sound_pack_method=sound_pack_method,
            sample_width=sample_width,
            channels_count=channels_count,
            unknown_04=unknown_04,
            frame_rate=frame_rate,
            frame_count=frame_count,
        )


class Wav(BinaryFormat):
    header: WavHeader
    frames: bytes

    @classmethod
    def from_file(cls, path: Path | str) -> Self:
        if isinstance(path, str):
            path = Path(path)

        with path.open("rb") as stream:
            return cls.from_stream(stream=stream)

    @classmethod
    def from_stream(cls, stream: BinaryIO) -> Self:
        header = WavHeader.from_stream(stream)
        frames = stream.read()

        return cls(
            header=header,
            frames=frames,
        )

    def to_waveform(self, path: Path | str):
        path = Path(path)

        with wave.open(path.as_posix(), mode="w") as waveform:
            waveform.setnchannels(self.header.channels_count)
            waveform.setsampwidth(self.header.sample_width // 8)
            waveform.setframerate(self.header.frame_rate)
            waveform.writeframesraw(self.frames)
