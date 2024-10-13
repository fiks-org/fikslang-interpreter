from dataclasses import dataclass

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class AddAll(Instruction):
    opcode = "ADD_ALL"

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        state.stack = [sum(state.stack)]
        return pc + 1
