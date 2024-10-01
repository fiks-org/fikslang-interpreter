from abc import abstractmethod
from dataclasses import dataclass
from typing import ClassVar, Self

from fikslang.src.memory_state import MemoryState


@dataclass
class Instruction:
    opcode: ClassVar[str]

    @classmethod
    def from_params(cls, params: list[str]) -> Self:
        """
        Create an instruction from a list of parameters
        :param params: List of parameters
        :return: Instruction
        """
        return cls()

    @abstractmethod
    def execute(self, state: MemoryState, pc: int, labels: dict[str, int]) -> int:
        """
        Execute the instruction on the given state
        :return: New PC
        """
        ...
