from dataclasses import dataclass
from datetime import UTC, datetime

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState

@dataclass
class Uptime(Instruction):
    opcode = "UPTIME"

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        state.stack.append(datetime.now(UTC) - state.start_time);
        return pc + 1