"""Workers nodes for execution pipeline"""

from src.workers.grep import Grep
from src.workers.readfile import Readfile
from src.workers.replace import Replace
from src.workers.sort import Sort
from src.workers.worker import Worker
from src.workers.writefile import Writefile

__author__="urmancheev"
__email__="matricarin@gmail.com"
__version__="0.1.0"
__all__= [
    "Grep",
    "Readfile",
    "Replace",
    "Sort",
    "Worker",
    "Writefile"
]