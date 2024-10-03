from dataclasses import dataclass
from typing import Self

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class Save(Instruction):
    opcode = "SAVE"

    to_save: int

    @classmethod
    def from_params(cls, params: list[str]) -> Self:
        return cls(to_save=int(params[0]))

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        idx = 0
        while idx in state.heap:
            idx += 1
        state.heap[idx] = self.to_save
        state.stack.append(idx)
        return pc + 1
