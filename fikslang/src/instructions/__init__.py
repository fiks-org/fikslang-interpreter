from typing import Type

from fikslang.src.instructions.clear import Clear
from fikslang.src.instructions.instruction import Instruction
from fikslang.src.instructions.jmp import Jump
from fikslang.src.instructions.nop import Nop
from fikslang.src.instructions.push import Push
from fikslang.src.instructions.rotate import Rotate
from fikslang.src.instructions.time import Time
from fikslang.src.instructions.unreachable import Unreachable

INSTRUCTIONS = [Clear, Rotate, Time, Nop, Push, Jump, Unreachable]


def find_instruction(opcode: str) -> Type[Instruction] | None:
    for instruction in INSTRUCTIONS:
        if instruction.opcode == opcode:
            return instruction
