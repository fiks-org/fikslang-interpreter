from dataclasses import dataclass

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState

@dataclass
class Sort(Instruction):
    opcode = "SORT"
    
    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        number_of_elements = state.stack.pop()
        if (number_of_elements == 0):
            return pc + 1
        sort_type = "ASC"
        if (number_of_elements < 0):
            number_of_elements = abs(number_of_elements)
            sort_type = "DESC"
        array = state.stack[-number_of_elements:]
        array.sort(reverse=sort_type == "DESC")
        state.stack = state.stack[:-number_of_elements] + array
        return pc + 1


        