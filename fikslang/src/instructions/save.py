from dataclasses import dataclass

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class Save(Instruction):
    opcode = "SAVE"

    to_save: int

    @classmethod
    def from_params(cls, params: list[str]) -> Save:
        return cls(to_save=int(params[0]))

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        freeIndex: int = len(state.heap)
        state.heap[freeIndex] = self.to_save
        state.stack.append(freeIndex)
        return pc + 1
    