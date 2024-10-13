import json
from datetime import datetime
from pathlib import Path

import pytest
import time_machine

from fikslang.src.machine import Machine

SOURCES_PATH = Path(__file__).parent / "sources"


@pytest.mark.parametrize(
    "test_name", ["time", "rotate", "jmp", "sort", "pack-unpack", "vecsub"]
)
@time_machine.travel(datetime(2024, 1, 29, 23, 30, 59))
def test_e2e(test_name: str):
    source = SOURCES_PATH / f"{test_name}.fiks"
    expected_result = SOURCES_PATH / f"{test_name}.json"

    source_code = source.read_text()
    expected = json.loads(expected_result.read_text())

    machine = Machine(source_code)

    machine.execute()

    assert machine.memory.stack == expected["stack"]
    assert machine.memory.heap == expected["heap"]


def test_infinite_jump():
    source = "JMP 0"

    machine = Machine(source)
    with pytest.raises(ValueError):
        machine.execute()
