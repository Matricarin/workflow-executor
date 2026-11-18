from src.pipeline.context import Context, DataType
from src.pipeline.worker import Worker


class Replace(Worker):
    
    def __init__(self, old_value:str, new_value:str):
        self._old_value = old_value
        self._new_value = new_value
    
    @property
    def name(self) -> str:
        return "replace"
    
    @property
    def output_type(self) -> DataType:
        return DataType.TEXT
    
    @property
    def input_type(self) -> DataType:
        return DataType.TEXT
    
    def run(self, context: Context) -> Context:
        if not context.text:
            return context
        source = context.text.splitlines()
        replaced = [line.replace(self._old_value, self._new_value) for line in source]
        return Context("\n".join(replaced))
    
    