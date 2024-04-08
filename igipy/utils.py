from collections import Counter
from pathlib import Path


def count_extensions(directory: Path) -> dict[str, int]:
    counter = Counter(path.suffix for path in directory.glob("**/*") if path.is_file())
    return dict(sorted(counter.items(), key=lambda kv: kv[1], reverse=True))
