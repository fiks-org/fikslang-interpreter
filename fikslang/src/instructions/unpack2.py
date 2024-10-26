from dataclasses import dataclass

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class Unpack2(Instruction):
    opcode = "UNPACK2"

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        x = state.stack.pop()
        iters = 0

        c = 0
        while x % 3 != 2:
            iters += 1
            if iters > 100_000:
                raise ValueError("UNPACK2: Infinite loop detected")

            c *= 2
            c += x % 3
            x //= 3
        x //= 3
        state.stack.append(x & (1 << c) - 1)
        state.stack.append(x >> c)
        return pc + 1
