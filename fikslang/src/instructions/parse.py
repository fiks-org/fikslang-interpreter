from dataclasses import dataclass
from typing import Self

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class Parse(Instruction):
    opcode = "PARSE"

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        string = str(state.stack.pop())
        for char in string:
            state.stack.append(int(char))
        return pc + 1
