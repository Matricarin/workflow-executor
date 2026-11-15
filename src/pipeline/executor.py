from src.workers import Worker


class Executor:
    """
    Execition pipeline
    """
    
    def __init__(self, workers: list[Worker]):
        self._workers = workers
        
    def execute(self) -> None:
        pass