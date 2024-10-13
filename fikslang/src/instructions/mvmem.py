from dataclasses import dataclass

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class MVmem(Instruction):
    opcode = "MVMEM"

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        idx = 0
        while idx in state.heap:
            idx += 1
        state.heap[idx] = state.stack[-1]
        state.stack.append(idx)
        return pc + 1
