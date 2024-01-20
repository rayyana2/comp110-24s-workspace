"""simple battleship - a cute step toward battleship."""

__author__ = "730656243"

# Assign p1 variables.
user_input: str = input("Pick a secret boat location between 1 and 4:")
ship_number_p1: int = int(user_input)

# p1 errors
if ship_number_p1 < 1:
    print(f"Error! {ship_number_p1} too low!")
    exit()
if ship_number_p1 > 4:
    print(f"Error! {ship_number_p1} too high!")
    exit()

# assign p2 variables
user_input2: str = input("Guess a number between 1 and 4:")
ship_number_p2: int = int(user_input2)

# p2 errors
if ship_number_p2 < 1:
    print(f"Error! {ship_number_p2} too low!")
    exit()
if ship_number_p2 > 4:
    print(f"Error! {ship_number_p2} too high!")
    exit()

# visual aid variables
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# victory or defeat
if ship_number_p2 == ship_number_p1:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")
    
if ship_number_p2 == ship_number_p1:
    print("Correct! You hit the ship.")
    result: str = RED_BOX
else:
    print("Incorrect! You missed the ship.")
    result: str = WHITE_BOX

# implementing visuals
if ship_number_p2 == 1:
    print(result + BLUE_BOX + BLUE_BOX + BLUE_BOX)
if ship_number_p2 == 2:
    print(BLUE_BOX + result + BLUE_BOX + BLUE_BOX)
if ship_number_p2 == 3:
    print(BLUE_BOX + BLUE_BOX + result + BLUE_BOX)
if ship_number_p2 == 4:
    print(BLUE_BOX + BLUE_BOX + BLUE_BOX + result)