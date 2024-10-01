from dataclasses import dataclass
from typing import Self

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class Push(Instruction):
    opcode = "PUSH"

    to_push: int

    @classmethod
    def from_params(cls, params: list[str]) -> Self:
        return cls(to_push=int(params[0]))

    def execute(self, state: MemoryState, pc: int) -> int:
        state.stack.append(self.to_push)

        return pc + 1
