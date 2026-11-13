from abc import ABC, abstractmethod

from src.pipeline import Context


class Worker(ABC):
    """
    Abstract class for nodes in pipeline
    """
    
    @abstractmethod
    def execute(self, context: Context) -> Context:
        pass