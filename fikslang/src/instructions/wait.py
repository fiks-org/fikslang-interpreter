import time
from dataclasses import dataclass
from typing import Self

from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState


@dataclass
class Wait(Instruction):
    opcode = "WAIT"

    time_to_wait: int

    @classmethod
    def from_params(cls, params: list[str]) -> Self:
        return cls(time_to_wait=int(params[0]))

    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        if self.time_to_wait / 1000 > 2:
            raise ValueError(
                "Computer feel asleep... Watchdog triggered process termination"
            )

        time.sleep(self.time_to_wait / 1000)
        return pc + 1
