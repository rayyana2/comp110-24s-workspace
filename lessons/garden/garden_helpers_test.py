"""Test my garden functions."""
__author__: str = "730656243"


from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date


def test_add_by_kind_new() -> None:
    """Tests the ability to add a new kind to a dictionary."""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    add_by_kind(by_kind, "tree", "apple")
    assert by_kind == {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"], "tree": ["apple"]}


def test_add_by_kind_empty() -> None:
    """Tests the ability to add an empty list to a new kind."""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    add_by_kind(by_kind, "tree", "")
    assert by_kind == {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"], "tree": [""]}


def test_add_by_date_new() -> None:
    """Tests the ability to add a new date to a dictionary."""
    by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    add_by_date(by_date, "January", "strawberries")
    assert by_date == {"April": ["marigold"], "June": ["carrots"], "January": ["strawberries"]}


def test_add_by_date_empty() -> None:
    """Tests the ability to add an empty list to a new date."""
    by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    add_by_date(by_date, "January", "")
    assert by_date == {"April": ["marigold"], "June": ["carrots"], "January": [""]}


def test_lookup_by_kind_and_date_success() -> None:
    """Tests the ability to provide the types of plants in a certain month."""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    assert lookup_by_kind_and_date(by_kind, by_date, "vegetable", "June") == "vegetables to plant in June: ['carrots']."


def test_lookup_by_kind_and_date_empty_kind() -> None:
    """Tests functionality when the dictionary of kinds is empty."""
    by_kind: dict[str, list[str]] = {"vegetable": []}
    by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    assert lookup_by_kind_and_date(by_kind, by_date, "vegetable", "June") == "No vegetables to plant in June."