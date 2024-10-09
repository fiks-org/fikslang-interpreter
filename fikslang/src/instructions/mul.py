from dataclasses import dataclass
from typing import Self

from fikslang.src.instructions import Instruction
from fikslang.src.memory_state import MemoryState

@dataclass
class Mul(Instruction):
    opcode = "MUL"

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        first = state.stack.pop();
        second = state.stack.pop();
        state.stack.append(first*second);
        return pc + 1