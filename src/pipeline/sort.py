from src.pipeline.context import Context, DataType
from src.pipeline.worker import Worker


class Sort(Worker):
    
    @property
    def name(self) -> str:
        return "sort"
    
    @property
    def output_type(self) -> DataType:
        return DataType.TEXT
    
    @property
    def input_type(self) -> DataType:
        return DataType.TEXT
    
    def run(self, context: Context) -> Context:
        if context.text:
            source = context.text.splitlines()
            ordered = sorted(source)
            return Context("\n".join(ordered))
        else:
            return context
        