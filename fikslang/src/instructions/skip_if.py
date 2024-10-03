from dataclasses import dataclass
from typing import Self

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.instructions.utils import is_jump_condition_true
from fikslang.src.memory_state import MemoryState


@dataclass
class SkipIf(Instruction):
    opcode = "SKIP_IF"
    condition: str

    @classmethod
    def from_params(cls, params: list[str]) -> Self:
        return cls(condition=params[0])

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        if is_jump_condition_true(self.condition, state.stack):
            return pc + 2
        else:
            return pc + 1
