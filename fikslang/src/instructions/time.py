from dataclasses import dataclass
from datetime import UTC, datetime

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class Time(Instruction):
    opcode = "TIME"

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        utc_now = datetime.now(UTC)

        state.stack.append(utc_now.second)
        state.stack.append(utc_now.minute)
        state.stack.append(utc_now.hour)

        return pc + 1
