from dataclasses import dataclass
from math import floor, log2

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState

@dataclass
class Unpack2(Instruction):
    opcode = "UNPACK2"

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        x = state.stack.pop()
        c = 0
        while x % 3 != 2:
            c *= 2
            c += x % 3
            x //= 3
        x //= 3
        state.stack.append(x & (1 << c)-1)
        state.stack.append(x >> c)
        return pc + 1