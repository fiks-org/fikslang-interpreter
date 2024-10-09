from dataclasses import dataclass

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState

@dataclass
class MaxIndex(Instruction):
    opcode = "MAX_INDEX"

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        max = state.stack[-1]
        max_index = len(state.stack)-1
        for i in range(len(state.stack)-1):
            if state.stack[i] > max:
                max = state.stack[i]
                max_index = i
        state.stack.append(max_index)
        return pc + 1   