"""Functions that either mutate a list or don't."""


def remove_first(input: list[str]) -> None:
    """Remove first element."""
    input.pop(0)

def get_first(input: list[str]) -> str:
    """Return first element."""
    return input[0]

def get_and_remove_first(input: list[str]) -> str:
    """Remove and return first element."""
    output: str = input[0]
    input.pop(0)
    return output