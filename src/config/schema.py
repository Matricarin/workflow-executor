from dataclasses import dataclass


@dataclass(frozen=True)
class BlockSpec:
    id:int | None = None
    command: str | None = None
    args: tuple[str, ...] | None = None 

@dataclass(frozen=True)
class Schema:
    blocks: set[BlockSpec] | None = None
    pipeline_ids: tuple[int, ...] | None = None