from typing import Protocol

from src.config.schema import BlockSpec, Schema
from src.exceptions import ConfigSyntaxError
from src.pipeline.worker import Worker


class WorkflowParser(Protocol):
    def parse(self, raw_text: str) -> Schema: ...


class Parser:
    
    def __init__(self, workers: list[Worker]) -> None:
        self._workers = workers
    
    def parse(self, raw_text: str) -> Schema:
        raw_text_lines: list[str] = raw_text.splitlines()
        lines_amount: int = len(raw_text_lines)
        pre_last: int = lines_amount - 2
        blocks: set[BlockSpec] = set()
        ids: tuple[int, ...] = ()
        for i in range(lines_amount):
            line: str = raw_text_lines[i]
            parts = line.partition('#')
            if not parts[0]:
                continue  
            current_line = parts[0]
            match i:
                case 0:
                    if current_line != "desc":
                        raise ConfigSyntaxError("Description must be started from \"desc\".")
                case _ if i == pre_last:
                    if current_line != "csed":
                        raise ConfigSyntaxError("BlockSpecs description must be end by \"csed\".")
                case _ if i == lines_amount - 1:
                    try:
                        ids = tuple(map(int, current_line.split(sep="->")))
                    except Exception:
                        raise ConfigSyntaxError("Last line parsing error.")              
                case _:
                    try:    
                                               
                        tokens: list[str] = current_line.split(sep=' ')     
                                                
                        id_str: str = tokens[0]
                        
                        if not str.isdigit(id_str) and float.is_integer(float(id_str)):
                            raise ConfigSyntaxError("Id for block in specification is not digit.")
                        
                        command: str = tokens[2]
                        
                        args: tuple[str, ...] = tuple(arg for arg in tokens[2:])
                        
                        block_spec = BlockSpec(id=int(id_str), command=command, args=args)
                        
                        blocks.add(block_spec)
                        
                    except IndexError:
                        raise ConfigSyntaxError("Syntax error. Please check blocks description.")                                 
         
        return Schema(blocks=blocks, pipeline_ids=ids)
