"""simple battleship - a cute step toward battleship."""

__author__ = "730656243"

user_input: str = input("Pick a secret boat location between 1 and 4:")
ship_number_p1: int = int(user_input)

if ship_number_p1 < 1:
    print(f"Error! {ship_number_p1} too low!")
if ship_number_p1 > 4:
    print(f"Error! {ship_number_p1} too high!")

user_input2: str = input("Pick a secret boat loacation between 1 and 4:")
ship_number_p2: int = int(user_input2)

if ship_number_p2 < 1:
    print(f"Error! {ship_number_p2} too low!")
if ship_number_p2 > 4:
    print(f"Error! {ship_number_p2} too high!")