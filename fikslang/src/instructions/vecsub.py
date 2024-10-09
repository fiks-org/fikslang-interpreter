from dataclasses import dataclass
from typing import Self

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState

@dataclass
class VecSub(Instruction):
    opcode = "VECSUB"

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        if len(state.stack) % 2 != 0:
            state.heap[1] = 42
            return pc + 1
        first_half = state.stack[-len(state.stack)//2:]
        second_half = state.stack[-len(state.stack)//2:]
        state.stack.clear()
        for i in range(len(first_half)):
            state.stack.append(first_half[i] - second_half[i])
        return pc + 1
