from dataclasses import dataclass

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class Nop(Instruction):
    opcode = "NOP"

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        return pc + 1
