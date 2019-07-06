from typing import Generator, TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


class FileGatherer:
    def gather_files(self, from_here: 'Path', this_type: str) -> Generator:
        return from_here.rglob(f"*.{this_type}")
