from dataclasses import dataclass
from typing import Self

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class Glue(Instruction):
    opcode = "GLUE"

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        string = ""
        while len(state.stack) > 0:
            string += str(state.stack.pop())
        state.stack.append(int(string))
        return pc + 1