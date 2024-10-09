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
from fikslang.src.instructions.modulo import Modulo
from fikslang.src.instructions.ret import Ret 
from fikslang.src.instructions.mul import Mul
from fikslang.src.instructions.pow import Pow
from fikslang.src.instructions.rotate import Rotate
from fikslang.src.instructions.save import Save
from fikslang.src.instructions.inc import Inc
from fikslang.src.instructions.skip_if import SkipIf 
from fikslang.src.instructions.parse import Parse   
from fikslang.src.instructions.time import Time
from fikslang.src.instructions.unreachable import Unreachable
from fikslang.src.instructions.wait import Wait
from fikslang.src.instructions.sort import Sort
from fikslang.src.instructions.delete import Delete 
from fikslang.src.instructions.max_index import MaxIndex
from fikslang.src.instructions.pack2 import Pack2
from fikslang.src.instructions.unpack2 import Unpack2
from fikslang.src.instructions.exit import Exit
from fikslang.src.instructions.vecsub import VecSub
from fikslang.src.instructions.uptime import Uptime

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
    Mul,
    Pow,
    Rotate,
    Save,
    SkipIf,
    Parse,
    Time,
    Unreachable,
    Wait,
    Modulo,
    Inc,
    Sort,
    Delete,
    MaxIndex,
    Pack2,
    Unpack2,
    Exit,
    Uptime,
    VecSub
]


def find_instruction(opcode: str) -> Type[Instruction] | None:
    for instruction in INSTRUCTIONS:
        if instruction.opcode == opcode:
            return instruction
