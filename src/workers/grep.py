from pipeline.context import Context, DataType
from src.workers.worker import Worker


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
        source: list[str] = context.text.split(sep="\n")
        filtered: list[str] = []
        for line in source:
            if line.__contains__(self._word):
                filtered.append(line)
        return Context("\n".join(filtered))
        