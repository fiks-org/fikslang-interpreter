from dataclasses import dataclass, field


@dataclass
class MemoryState:
    stack: list[int] = field(default_factory=list)
    heap: dict[int, int] = field(default_factory=dict)
