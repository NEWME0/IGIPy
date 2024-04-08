from collections import Counter
from pathlib import Path
from typing import Self, BinaryIO

from pydantic import BaseModel


def count_extensions(directory: Path) -> dict[str, int]:
    counter = Counter(path.suffix for path in directory.glob("**/*") if path.is_file())
    return dict(sorted(counter.items(), key=lambda kv: kv[1], reverse=True))


class BinaryFormat(BaseModel):
    @classmethod
    def from_stream(cls, stream: BinaryIO) -> Self:
        raise NotImplementedError()

    @classmethod
    def from_file(cls, path: Path | str) -> Self:
        path = Path(path)

        if not path.exists():
            raise FileNotFoundError(f"Not found a file at: {path.as_posix()}")

        if not path.is_file():
            raise FileNotFoundError(f"Found something else than file at: {path.as_posix()}")

        with path.open(mode="rb") as stream:
            return cls.from_stream(stream)
