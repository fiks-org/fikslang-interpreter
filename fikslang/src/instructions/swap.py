from dataclasses import dataclass

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class Swap(Instruction):
    opcode = "SWAP"

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        state.stack[-1], state.stack[-2] = state.stack[-2], state.stack[-1]

        return pc + 1
