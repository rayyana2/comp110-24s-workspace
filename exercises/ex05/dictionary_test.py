"""Test functions for dictionary.py."""
__author__ = "730656243"


from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_two_elements() -> None:
    """Input of a dictionary with two keys should flip the keys and elements."""
    assert invert({"blue": "one", "red": "two"}) == {"one": "blue", "two": "red"}


def test_invert_one_element() -> None:
    """Input of a dictionary with one key should flip the key and element."""
    assert invert({"blue": "one"}) == {"one": "blue"}


def test_invert_key_error() -> None:
    """Input list with duplicate elements will raise a key error."""
    import pytest
    with pytest.raises(KeyError):
        dictionary = {"blue": "one", "red": "one"}
        invert(dictionary)


def test_favorite_color_most_frequent() -> None:
    """Should output the most frequent color in a dictionary."""
    assert favorite_color({"Carla": "green", "Jacob": "green", "Jose": "blue"}) == "green"


def test_favorite_color_string() -> None:
    """Output is a string of the favorite color, not an integer of the count."""
    assert type(favorite_color({"Carla": "green", "Jacob": "green", "Jose": "blue"})) == str


def test_favorite_color_if_not_color() -> None:
    """Confirms that the function works with any string, not just colors."""
    assert favorite_color({"Carla": "dog", "Jacob": "dog", "Jose": "frog"}) == "dog"


def test_count_one_object() -> None:
    """An input of one object should return a dictionary with one key and a count of one."""
    assert count(["dog"]) == {"dog": 1}


def test_count_duplicate() -> None:
    """Multiple of the same object should increase the count in the output."""
    assert count(["dog", "dog"]) == {"dog": 2}


def test_count_with_int() -> None:
    """Count function works with integers, not just strings."""
    assert count([1, 1]) == {1: 2}


def test_alphabetizer_one() -> None:
    """An input of one object should result in an output with one key."""
    assert alphabetizer(["dog"]) == {"d": ["dog"]}


def test_alphabetizer_duplicate() -> None:
    """More than one word with the same starting letter should appear together."""
    assert alphabetizer(["dog", "dozen"]) == {"d": ["dog", "dozen"]}


def test_alphabetizer_all_caps() -> None:
    """An input list in all capital letters will output with lowercase keys."""
    assert alphabetizer(["DOG", "DOZEN"]) == {"d": ["DOG", "DOZEN"]}


def test_update_attendance_preexisting() -> None:
    """Adding a student to a dictionary on a day that is already present will update that day."""
    attendance: dict[str, list[str]] = {"Tuesday": ["Carla", "Jacob"]}
    update_attendance(attendance, "Tuesday", "Jose")
    assert attendance == {"Tuesday": ["Carla", "Jacob", "Jose"]}


def test_update_attendance_new() -> None:
    """Adding a student to a day that is not already in the list will create a new day."""
    attendance: dict[str, list[str]] = {"Tuesday": ["Carla", "Jacob"]}
    update_attendance(attendance, "Wednesday", "Jose")
    assert attendance == {"Tuesday": ["Carla", "Jacob"], "Wednesday": ["Jose"]}


def test_update_attendance_integer() -> None:
    """Can add integers to the dictionary instead of students."""
    attendance: dict[str, list[str]] = {"Tuesday": ["Carla", "Jacob"]}
    update_attendance(attendance, "Tuesday", 4)
    assert attendance == {"Tuesday": ["Carla", "Jacob", 4]}