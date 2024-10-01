from dataclasses import dataclass

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class Clear(Instruction):
    opcode = "CLEAR"

    def execute(self, state: MemoryState, pc: int) -> int:
        state.stack.clear()
        return pc + 1
