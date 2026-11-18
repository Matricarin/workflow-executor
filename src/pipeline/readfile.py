from src.io.file_reader import FileReader
from src.pipeline.context import Context, DataType
from src.pipeline.worker import Worker


class Readfile(Worker):
    
    def __init__(self, path:str, reader:FileReader | None = None):
            self._path = path
            self._reader = reader or FileReader()
        
    @property
    def name(self) -> str:
        return "readfile"
    
    @property
    def output_type(self) -> DataType:
        return DataType.TEXT
    
    @property
    def input_type(self) -> DataType:
        return DataType.NONE
    
    def run(self, context: Context) -> Context:
        text = self._reader.read_all(self._path)
        return Context(text)