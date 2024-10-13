from dataclasses import dataclass

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class Dup(Instruction):
    opcode = "DUP"

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        state.stack.append(state.stack[-1])
        return pc + 1
