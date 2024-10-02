from dataclasses import dataclass
from typing import Self

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class Proc(Instruction):
    opcode = "PROC"

    jump_to: int

    @classmethod
    def from_params(cls, params: list[str]) -> Self:
        return cls(jump_to=int(params[0]))

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        state.stack.append(pc + 1)
        pc = self.jump_to
        return pc