"""List utility functions."""
__author__ = "730656243"


def all(input_list: list[int], num: int) -> bool:
    """Checks if all objects in input_list are equal to num."""
    list_idx: int = 0
    while list_idx < len(input_list):
        if input_list[list_idx] != num:
            return False
        else:
            list_idx += 1
    return True


def max(max_list: list[int]) -> int:
    """Returns highest value in a list."""
    if len(max_list) == 0:
        raise ValueError("max() arg is an empty List")
    max_idx: int = 1
    max_num: int = max_list[0]
    while max_idx < len(max_list):
        if max_list[max_idx] > max_num:
            max_num = max_list[max_idx]
        max_idx += 1
    return max_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Returns whether the two lists are equal to each other or not."""
    if len(list1) == len(list2):
        list_idx: int = 0
        while list_idx < len(list1):
            if list1[list_idx] != list2[list_idx]:
                return False
            else:
                list_idx += 1
        return True
    else:
        return False


def extend(list1: list[int], list2: list[int]) -> None:
    """Adds list2 to the end of list1."""
    list_idx: int = 0
    while list_idx < len(list2):
        list1.append(list2[list_idx])
        list_idx += 1