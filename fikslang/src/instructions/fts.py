import json
from dataclasses import dataclass
from pathlib import Path
from typing import Self

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class FTS(Instruction):
    opcode = "FTS"
    filename: int

    @classmethod
    def from_params(cls, params: list[str]) -> Self:
        return cls(filename=int(params[0]))

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        target = Path("usersaves") / f"{self.filename}.fiksStack"
        loaded_stack = json.loads(target.read_text())

        state.stack.extend(loaded_stack)

        return pc + 1
