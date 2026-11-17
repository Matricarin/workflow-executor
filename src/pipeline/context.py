from dataclasses import dataclass
from enum import Enum, auto


class DataType(Enum):
    NONE = auto()
    TEXT = auto()
    
@dataclass(frozen=True)
class Context:
    text:str | None = None