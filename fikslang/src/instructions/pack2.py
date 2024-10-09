from dataclasses import dataclass
from math import floor, log2

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState

@dataclass
class Pack2(Instruction):
    opcode = "PACK2"

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        a = state.stack.pop()
        b = state.stack.pop()
        bl = 0
        if b == 0:
            bl = 1
        else:
            bl = floor(log2(b))+1
        c = 0
        cl = 0
        bl2 = bl
        while bl != 0:
            c *= 3
            c += bl % 2
            bl //= 2
            cl += 1
        state.stack.append((((a << bl2) + b)*3 + 2) * 3 ** cl + c)
        return pc + 1