from dataclasses import dataclass
from typing import Self

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class Get(Instruction):
    opcode = "GET"
    idx: int
    count: int

    @classmethod
    def from_params(cls, params: list[str]) -> Self:
        return cls(idx=int(params[0]), count=int(params[1]))

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        for i in range(self.count):
            state.stack.append(state.heap[self.idx + i])

        return pc + 1
