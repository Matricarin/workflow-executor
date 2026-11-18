from src.pipeline.context import Context, DataType
from src.pipeline.worker import Worker


class Grep(Worker):
    
    def __init__(self, word: str):
        self._word = word
    
    @property
    def name(self) -> str:
        return 'grep'
    
    @property
    def input_type(self) -> DataType:
        return DataType.TEXT
    
    @property
    def output_type(self) -> DataType:
        return DataType.TEXT
    
    def run(self, context: Context) -> Context:
        if not context.text:
            return context
        source: list[str] = context.text.splitlines()
        filtered: list[str] = [line for line in source if self._word in line]
        return Context("\n".join(filtered))
        