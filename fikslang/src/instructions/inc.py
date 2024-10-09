from dataclasses import dataclass

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class Inc(Instruction):
    opcode = "INC"

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        state.stack[-1] += 1
        return pc + 1