from pathlib import Path


class FileReader:
    def read_all(self, path:str | Path) -> str:
        with Path(path).open('r', encoding="utf-8") as file:
            return file.read()