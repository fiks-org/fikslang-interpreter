from dataclasses import dataclass
from typing import Self

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState

@dataclass
class Modulo(Instruction):
    opcode = "MODULO"

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        firstNumber = state.stack.pop();
        secondNumber = state.stack.pop();
        while firstNumber > secondNumber:
            firstNumber -= secondNumber;
        state.stack.append(firstNumber);
        return pc + 1