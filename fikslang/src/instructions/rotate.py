from dataclasses import dataclass
from typing import Self

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class Rotate(Instruction):
    opcode = "ROTATE"
    rotate_elements: int

    @classmethod
    def from_params(cls, params: list[str]) -> Self:
        return cls(rotate_elements=int(params[0]))

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        to_rotate = state.stack[-self.rotate_elements :]
        rotated = reversed(to_rotate)
        state.stack = state.stack[: -self.rotate_elements] + list(rotated)
        return pc + 1
