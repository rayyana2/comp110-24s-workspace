"""Test sum functionality."""

from lessons.sum import w_sum

def test_sum_empty() -> None:
    """Sum of empty list should return 0."""
    assert w_sum([]) == 0

def test_sum_positive() -> None:
    """Sum of positive numbers should return sum of those numbers."""
    test: list[int] = [2, 4, 6]
    assert w_sum(test) == 12

def test_sum_one_element() -> None:
    test: list[int] = [7]
    assert w_sum(test) == 7

def test_sum_with_negatives() -> None:
    test: list[int] = [2, -2, 4]
    assert w_sum(test) == 4