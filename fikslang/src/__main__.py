import json
import sys
from contextlib import suppress

from fikslang.src.machine import Machine


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: fikslang <source> (state.json)")
        print()
        print("Source file contains source code to execute.")
        print()
        print("State.json is optional. If it is present, it should contain")
        print('two fields: "stack" (int[]) and "memory" (map[int, int]).')
        return

    with open(sys.argv[1], "r") as f:
        source = f.read()

    if len(sys.argv) == 3:
        # We probably received state file as well
        with open(sys.argv[2], "r") as f:
            state = json.load(f)
    else:
        state = None

    try:
        machine = Machine(source)

        if state is not None:
            machine.memory.stack = state["stack"]
            machine.memory.heap = {int(k): v for k, v in state["memory"].items()}

        with suppress(SystemExit):
            machine.execute()

        if sys.stdout.isatty():
            print("Stack:")
            print(machine.memory.stack)
            print("Memory:")
            print(machine.memory.heap)
        else:
            print(
                json.dumps(
                    {
                        "stack": machine.memory.stack,
                        "memory": machine.memory.heap,
                        "instructions": [
                            instruction.opcode
                            for instruction in machine.execution_memory
                        ],
                    }
                )
            )
    except Exception as e:
        message = "Error: " + str(e)

        if sys.stdout.isatty():
            print(message)
        else:
            print(json.dumps({"error": message}))

        sys.exit(1)


if __name__ == "__main__":
    main()
