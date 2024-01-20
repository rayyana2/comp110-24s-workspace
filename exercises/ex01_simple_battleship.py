"""simple battleship - a cute step toward battleship."""

__author__ = "730656243"

user_input: str = input("Pick a secret boat location between 1 and 4:")
ship_number: int = int(user_input)

if ship_number < 1 or ship_number > 4:
    print(f"Error! {ship_number} too low!")