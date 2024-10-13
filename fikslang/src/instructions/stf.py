import json
from dataclasses import dataclass
from pathlib import Path
from typing import Self

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class STF(Instruction):
    opcode = "STF"
    limit: int | None

    @classmethod
    def from_params(cls, params: list[str]) -> Self:
        return cls(limit=-int(params[0]) if len(params) >= 1 else None)

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        target = Path("usersaves") / f"{state.stack[-1]}.fiksStack"

        target.write_text(json.dumps(state.stack[self.limit :]))

        return pc + 1
