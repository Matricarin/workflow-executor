from src.io.file_writer import FileWriter
from src.pipeline.context import Context, DataType
from src.pipeline.worker import Worker


class Writefile(Worker):
    
    def __init__(self, path:str, writer: FileWriter | None):
               self._path = path
               self._writer = writer or FileWriter()
           
    @property
    def name(self) -> str:
        return "writefile"
    
    @property
    def output_type(self) -> DataType:
        return DataType.TEXT
    
    @property
    def input_type(self) -> DataType:
        return DataType.NONE
    
    def run(self, context: Context) -> Context:
        if context.text:
            self._writer.write_all(self._path, context.text)
        else:
            self._writer.write_all(self._path, "")
        return context