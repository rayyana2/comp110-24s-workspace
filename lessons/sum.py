"""Summing the elements of a list using different loops."""
__author__ = "730656243"


def w_sum(vals: list[float]) -> float:
    """Sums a list using while loop."""
    if len(vals) == 0:
        sum: float = 0.0
        return sum
    idx: int = 1
    sum = vals[0]
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Sums a list using for loop."""
    sum: float = 0.0
    if len(vals) == 0:
        return sum
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Sums a list using for loop with range."""
    sum: float = 0.0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum