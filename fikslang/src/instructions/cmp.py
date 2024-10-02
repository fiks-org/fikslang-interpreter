from dataclasses import dataclass

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class Cmp(Instruction):
    opcode = "CMP" 
    
    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        #If the top of the stack is greater then the second, then save 1 to the stack else save -1 if they are equal save 0 if they are not equal
        #TODO: Handle stack underflow
        if state.stack[-1] > state.stack[-2]:
            state.stack.append(1)
        elif state.stack[-1] == state.stack[-2]:
            state.stack.append(0)
        else:
            state.stack.append(-1)
        return pc + 1