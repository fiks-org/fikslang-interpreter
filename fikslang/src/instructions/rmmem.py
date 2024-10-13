from dataclasses import dataclass

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class RMmem(Instruction):
    opcode = "RMMEM"

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        del state.heap[state.stack[-1]]
        return pc + 1
