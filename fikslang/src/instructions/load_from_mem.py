from dataclasses import dataclass

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class LoadFromMem(Instruction):
    opcode = "LOAD_FROM_MEM"

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        state.stack.append(state.heap.get(state.stack.pop(), -1))

        return pc + 1
