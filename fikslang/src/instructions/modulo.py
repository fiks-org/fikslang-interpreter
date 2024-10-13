from dataclasses import dataclass

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class Modulo(Instruction):
    opcode = "MODULO"

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        first = state.stack.pop()
        second = state.stack.pop()

        state.stack.append(first % second)
        return pc + 1
