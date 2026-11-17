from abc import ABC, abstractmethod

from src.pipeline.context import Context


class Worker(ABC):
    """
    Abstract class for nodes in pipeline
    """
    
    @property
    @abstractmethod
    def name(self) -> str:
        pass
    
    @abstractmethod
    def run(self, context: Context) -> Context:
        pass