from dataclasses import dataclass

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class Ret(Instruction):
    opcode = "RET"

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        return state.stack.pop()