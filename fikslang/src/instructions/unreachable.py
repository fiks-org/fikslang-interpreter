from dataclasses import dataclass

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class Unreachable(Instruction):
    opcode = "UNREACHABLE"

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        raise ValueError("Unreachable instruction reached")
