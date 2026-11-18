from abc import ABC, abstractmethod

from src.pipeline.context import Context, DataType


class Worker(ABC):
    ''' Base class for nodes in pipeline '''
    
    @property
    @abstractmethod
    def name(self) -> str:
        ''' Node name '''
        ...
        
    @property
    @abstractmethod
    def output_type(self) -> DataType:
        ''' Output data type '''
        ...
    
    @property
    @abstractmethod
    def input_type(self) -> DataType:
        ''' Input data type '''
        ...
    
    @abstractmethod
    def run(self, context: Context) -> Context:
        ''' Nodes business logic '''
        ...