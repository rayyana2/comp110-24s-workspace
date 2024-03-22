"""Some functions for my garden plan!"""
__author__: str = "730656243"


by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}


def add_by_kind(input: dict[str, list[str]], type: str, plant: str) -> None:
    """Adds a plant to a list based on its kind."""
    if type in input:
        input[type].append(plant)
    else:
        input[type] = [plant]


def add_by_date(input: dict[str, list[str]], date: str, plant: str) -> None:
    """Adds a plant to a list based on its planting month."""
    if date in input:
        input[date].append(plant)
    else:
        input[date] = [plant]


def lookup_by_kind_and_date(type_dict: dict[str, list[str]], date_dict: dict[str, list[str]], type: str, date: str) -> str:
    """Searches two dictionaries to find which plants of a certain type to plant in a certain month."""
    assert type in type_dict
    assert date in date_dict
    plant_list: list[str] = []
    for plant in type_dict[type]:
        if plant in date_dict[date]:
            plant_list.append(plant)
    if len(plant_list) == 0:
        return f"No {type}s to plant in {date}."
    else:
        return f"{type}s to plant in {date}: {plant_list}."