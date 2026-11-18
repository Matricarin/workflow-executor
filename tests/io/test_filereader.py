from pathlib import Path

from src.io.file_reader import FileReader


def test_read_test_data1_by_path():
    path = Path("tests/test_data/test_data1.txt")
    reader = FileReader()
    content = reader.read_all(path)
    
    assert content
    
    lines = content.splitlines()
    assert len(lines) == 4