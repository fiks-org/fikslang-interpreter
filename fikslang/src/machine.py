from fikslang.src.instructions import find_instruction
from fikslang.src.instructions.instruction import Instruction
from fikslang.src.memory_state import MemoryState

MAX_INSTRUCTIONS = 5000


class Machine:
    memory: MemoryState
    pc: int

    execution_memory: list[Instruction]
    labels: dict[str, int]

    def __init__(self, source: str):
        self.memory = MemoryState()
        self.pc = 0
        self.execution_memory = []
        self.labels = {}

        for line_counter, line in enumerate(source.split("\n")):
            line = line.strip(" ")

            if line == "" or line.startswith("#"):
                continue

            next_pc = len(self.execution_memory)

            words = line.strip().split(" ")

            if words[0].endswith(":"):
                label_name = words[0][:-1]
                self.labels[label_name] = next_pc
            else:
                # Try to find an instruction
                opcode = words[0].upper()
                instruction = find_instruction(opcode)
                if instruction is None:
                    raise ValueError(
                        f"Unknown opcode: {opcode} (on line {line_counter+1})"
                    )

                try:
                    self.execution_memory.append(instruction.from_params(words[1:]))
                except IndexError as e:
                    raise ValueError(
                        f"Invalid number of parameters for {opcode}. (on line {line_counter+1})"
                    ) from e
                except ValueError as e:
                    raise ValueError(
                        f"Invalid parameter for {opcode} (maybe a string instead of a number?). (on line {line_counter+1})"
                    ) from e

    def execute(self) -> None:
        instructions_executed = 0

        while self.pc < len(self.execution_memory):
            instruction = self.execution_memory[self.pc]
            self.pc = instruction.execute(self.memory, self.pc, self.labels)

            instructions_executed += 1
            if instructions_executed >= MAX_INSTRUCTIONS:
                raise ValueError("Maximum number of instructions executed exceeded")
