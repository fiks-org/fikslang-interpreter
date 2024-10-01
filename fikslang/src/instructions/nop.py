from dataclasses import dataclass

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class Nop(Instruction):
    opcode = "NOP"

    def execute(self, _state: MemoryState, pc: int) -> int:
        return pc + 1
