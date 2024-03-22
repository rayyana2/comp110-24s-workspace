"""Practice with dictionary functions."""
__author__ = "730656243"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Changes keys to values and vice versa."""
    inverted_list: dict[str, str] = {}
    for key in input:
        if input[key] in inverted_list:
            raise KeyError("Duplicate keys cannot exist.")
        inverted_list[input[key]] = key
    return inverted_list


def favorite_color(input: dict[str, str]) -> str:
    """Returns most frequent favorite color."""
    color_count: dict[str, int] = {}

    # Add colors and their frequencies to a new dictionary.
    for name in input:
        if input[name] in color_count:
            color_count[input[name]] += 1
        else:
            color_count[input[name]] = 1

    # Find the color in the new dictionary with the highest count and return that color.
    max_number: int = 0
    max_color: str = ""
    for color in color_count:
        if color_count[color] > max_number:
            max_number = color_count[color]
            max_color = color
    return max_color


def count(input: list[str]) -> dict[str, int]:
    """Returns the count of each item in a list."""
    count_dict: dict[str, int] = {}

    # Adds count of each object in the list to a dictionary.
    for elem in input:
        if elem in count_dict:
            count_dict[elem] += 1
        else:
            count_dict[elem] = 1
    return count_dict


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Organizes a list by the first letter of each word."""
    output: dict[str, list[str]] = {}
    for elem in input:
        if elem[0].lower() in output:
            output[elem[0].lower()].append(elem)
        else:
            output[elem[0].lower()] = [elem]
    return output


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Mutates a dictionary to update it with attendance information."""
    if day in attendance:
        if student not in attendance[day]:
            attendance[day].append(student)
    else:
        attendance[day] = [student]