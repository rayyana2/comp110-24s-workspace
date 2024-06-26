"""Battleship with grid."""
__author__: str = "730656243"

# grid variables
grid_size: int = 4
secret_row: int = 3
secret_column: int = 2
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# prompt user to guess row and column
row_guess: int = int(input("Guess a row: "))
while row_guess > grid_size or row_guess < 1:
    row_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

column_guess: int = int(input("Guess a column: "))
while column_guess > grid_size or column_guess < 1:
    column_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

# result boxes
if row_guess == secret_row and column_guess == secret_column:
    result_box: str = RED_BOX
else:
    result_box = WHITE_BOX

# making the picture
row_index: int = 1
while row_index <= grid_size:
    row_string: str = ""
    column_index: int = 1
    if row_guess == row_index:
        while column_index <= grid_size:
            if column_guess == column_index:
                row_string += result_box
            else:
                row_string += BLUE_BOX
            column_index += 1
    else:
<<<<<<< HEAD
        row_string += BLUE_BOX * grid_size
=======
        row_string += BLUE_BOX*grid_size
>>>>>>> 3917b5b5f26c118e61b4b183c2ce1c4f2157d7cf
    print(row_string)
    row_index = row_index + 1

# results in words
if row_guess == secret_row and column_guess == secret_column:
    print("Hit!")
elif row_guess == secret_row:
    print("Close! Correct row, wrong column.")
elif column_guess == secret_column:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")