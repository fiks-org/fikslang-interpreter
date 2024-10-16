from dataclasses import dataclass

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class MaxIndex(Instruction):
    opcode = "MAX_INDEX"

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        max_key = max(state.heap.keys())
        state.stack.append(max_key)
        return pc + 1
