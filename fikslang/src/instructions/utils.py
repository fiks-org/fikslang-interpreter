def is_jump_condition_true(condition: str, stack: list[int]) -> bool:
    match condition.upper():
        case "GT0":
            return stack[-1] > 0
        case "LE0":
            return stack[-1] <= 0
        case "LT0":
            return stack[-1] < 0
        case "GE0":
            return stack[-1] >= 0
        case "EQ0":
            return stack[-1] == 0
        case "NE0":
            return stack[-1] != 0
        case _:
            raise ValueError(f"Unknown jump condition: {condition}")
