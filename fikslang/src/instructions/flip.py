from dataclasses import dataclass

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class Flip(Instruction):
    opcode = "FLIP"

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        state.stack.reverse()
        return pc + 1
