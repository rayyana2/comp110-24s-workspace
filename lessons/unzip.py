"""Splitting a dict4ionary into two lists."""
__author__ = "730656243"


def get_keys(d: dict[str, int]) -> list[str]:
    """Adds keys in a dictionary to a new list."""
    l: list[str] = []
    for key in d:
        l.append(key)
    return l


def get_values(d: dict[str, int]) -> list[int]:
    """Adds values in a dictionary to a new list."""
    l: list[int] = []
    for key in d:
        l.append(d[key])
    return l