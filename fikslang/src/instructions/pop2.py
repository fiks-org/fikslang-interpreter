from dataclasses import dataclass

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class Pop2(Instruction):
    opcode = "POP2"

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        state.stack.pop(-2)
        return pc + 1
