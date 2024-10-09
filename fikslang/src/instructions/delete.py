from dataclasses import dataclass
from typing import Self

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState

@dataclass
class Delete(Instruction):
    opcode = "DELETE"

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        count = state.stack.pop()
        for _ in range(count):
            state.stack.pop()
        return pc + 1 