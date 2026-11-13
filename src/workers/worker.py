from abc import ABC, abstractmethod

from src.pipeline import Context


class Worker(ABC):
    """
    Abstract class for nodes in pipeline
    """
    
    @property
    @abstractmethod
    def name(self) -> str:
        pass
    
    @abstractmethod
    def execute(self, context: Context) -> Context:
        pass