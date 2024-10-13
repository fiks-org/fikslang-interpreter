from dataclasses import dataclass
from typing import Self

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class Len(Instruction):
    opcode = "LEN"
    target: int

    @classmethod
    def from_params(cls, params: list[str]) -> Self:
        return cls(target=int(params[0]))

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        state.heap[self.target] = len(state.stack)
        return pc + 1
