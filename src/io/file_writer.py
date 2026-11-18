from pathlib import Path


class FileWriter:
    def write_all(self, path:str | Path, text:str) -> None:
        with Path(path).open('w', encoding="utf-8") as file:
            file.write(text)