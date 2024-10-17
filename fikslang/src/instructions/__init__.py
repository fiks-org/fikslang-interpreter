from typing import Type

from fikslang.src.instructions.add_all import AddAll
from fikslang.src.instructions.clear import Clear
from fikslang.src.instructions.cmp import Cmp
from fikslang.src.instructions.delete import Delete
from fikslang.src.instructions.dup import Dup
from fikslang.src.instructions.exit import Exit
from fikslang.src.instructions.flip import Flip
from fikslang.src.instructions.fts import FTS
from fikslang.src.instructions.get import Get
from fikslang.src.instructions.glue import Glue
from fikslang.src.instructions.inc import Inc
from fikslang.src.instructions.instruction import Instruction
from fikslang.src.instructions.jmp import Jump
from fikslang.src.instructions.len import Len
from fikslang.src.instructions.load_from_mem import LoadFromMem
from fikslang.src.instructions.max_index import MaxIndex
from fikslang.src.instructions.modulo import Modulo
from fikslang.src.instructions.mul import Mul
from fikslang.src.instructions.mvmem import MVmem
from fikslang.src.instructions.nop import Nop
from fikslang.src.instructions.pack2 import Pack2
from fikslang.src.instructions.parse import Parse
from fikslang.src.instructions.pop2 import Pop2
from fikslang.src.instructions.pow import Pow
from fikslang.src.instructions.proc import Proc
from fikslang.src.instructions.push import Push
from fikslang.src.instructions.ret import Ret
from fikslang.src.instructions.rmmem import RMmem
from fikslang.src.instructions.rotate import Rotate
from fikslang.src.instructions.save import Save
from fikslang.src.instructions.skip_if import SkipIf
from fikslang.src.instructions.sort import Sort
from fikslang.src.instructions.stf import STF
from fikslang.src.instructions.swap import Swap
from fikslang.src.instructions.time import Time
from fikslang.src.instructions.unpack2 import Unpack2
from fikslang.src.instructions.unreachable import Unreachable
from fikslang.src.instructions.vecsub import VecSub
from fikslang.src.instructions.wait import Wait

INSTRUCTIONS: list[Type[Instruction]] = [
    AddAll,
    Clear,
    Cmp,
    Delete,
    Dup,
    Exit,
    Flip,
    FTS,
    Get,
    Glue,
    Inc,
    Jump,
    Len,
    LoadFromMem,
    MaxIndex,
    Modulo,
    Mul,
    MVmem,
    Nop,
    Pack2,
    Parse,
    Pop2,
    Pow,
    Proc,
    Push,
    Ret,
    Rotate,
    RMmem,
    Save,
    SkipIf,
    Sort,
    STF,
    Swap,
    Time,
    Unpack2,
    Unreachable,
    VecSub,
    Wait,
]


def find_instruction(opcode: str) -> Type[Instruction] | None:
    for instruction in INSTRUCTIONS:
        if instruction.opcode == opcode:
            return instruction
