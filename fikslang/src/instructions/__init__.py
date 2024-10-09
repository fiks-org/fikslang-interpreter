from typing import Type

from fikslang.src.instructions.clear import Clear
from fikslang.src.instructions.cmp import Cmp
from fikslang.src.instructions.glue import Glue
from fikslang.src.instructions.flip import Flip
from fikslang.src.instructions.instruction import Instruction
from fikslang.src.instructions.jmp import Jump
from fikslang.src.instructions.nop import Nop
from fikslang.src.instructions.proc import Proc
from fikslang.src.instructions.push import Push
from fikslang.src.instructions.ret import Ret
from fikslang.src.instructions.rotate import Rotate
from fikslang.src.instructions.modulo import Modulo
from fikslang.src.instructions.save import Save
from fikslang.src.instructions.skip_if import SkipIf 
from fikslang.src.instructions.parse import Parse
from fikslang.src.instructions.time import Time
from fikslang.src.instructions.unreachable import Unreachable
from fikslang.src.instructions.wait import Wait

INSTRUCTIONS: list[Type[Instruction]] = [
    Clear,
    Cmp,
    Glue,
    Flip,
    Jump,
    Nop,
    Proc,
    Push,
    Ret,
    Rotate,
    Save,
    SkipIf,
    Parse,
    Time,
    Unreachable,
    Wait,
    Modulo,
]


def find_instruction(opcode: str) -> Type[Instruction] | None:
    for instruction in INSTRUCTIONS:
        if instruction.opcode == opcode:
            return instruction
