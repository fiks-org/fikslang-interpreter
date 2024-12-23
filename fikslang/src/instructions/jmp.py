from dataclasses import dataclass
from typing import Self

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class Jump(Instruction):
    opcode = "JMP"
    target: str

    @classmethod
    def from_params(cls, params: list[str]) -> Self:
        return cls(target=params[0])

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        try:
            return int(self.target) + pc  # relative jump
        except ValueError:
            # probably is a label
            return labels[self.target]  # absolute jump
