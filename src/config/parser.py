from typing import Protocol

from src.config.schema import BlockSpec, Schema
from src.exceptions import ConfigSyntaxError


class WorkflowParser(Protocol):
    def parse(self, raw_text: str) -> Schema: ...


class Parser:
    def parse(self, raw_text: str) -> Schema:
        # TO-DO
        return Schema()
