"""Mutating functions."""
__author__ = "730656243"


def manual_append(a: list[int], number: int) -> None:
    """Adds input to the end of list."""
    a.append(number)


def double(b: list[int]) -> None:
    """Doubles each object in a list."""
    b_index: int = 0
    while b_index < len(b):
        b[b_index] *= 2
        b_index += 1