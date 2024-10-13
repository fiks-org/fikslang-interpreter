from dataclasses import dataclass

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class VecSub(Instruction):
    opcode = "VECSUB"

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        if len(state.stack) % 2 != 0:
            state.heap[1] = 42
            return pc + 1

        first = state.stack[::2]
        second = state.stack[1::2]
        state.stack.clear()

        for i in range(len(first)):
            state.stack.append(first[i] - second[i])

        return pc + 1
