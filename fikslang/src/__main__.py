import json
import sys

from fikslang.src.machine import Machine


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: fikslang <source>")
        return

    with open(sys.argv[1], "r") as f:
        source = f.read()

    try:
        machine = Machine(source)
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
