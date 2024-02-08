"""Battleship using function implementation."""
__author__: str = "730656243"
import random

def input_guess(grid_size: int, row_or_column: str) -> int:
    assert row_or_column == "row" or row_or_column == "column"
    if row_or_column == "row":
        row_guess: int = int(input("Guess a row: "))
        while row_guess < 1 or row_guess > grid_size:
            row_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
        return row_guess
    else:
        column_guess: int = int(input("Guess a column: "))
        while column_guess < 1 or column_guess > grid_size:
            column_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
        return column_guess

def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    if row_guess == secret_row and column_guess == secret_column:
        return True
    else:
        return False

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

def print_grid(grid_size: int, row_guess: int, column_guess: int, correct: bool) -> None:
    if correct:
        result_box: str = RED_BOX
    else:
        result_box = WHITE_BOX
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
            row_string += BLUE_BOX * grid_size
        print(row_string)
        row_index = row_index + 1

def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    grid_size = grid_size
    secret_row: int = secret_row
    secret_column: int = secret_column
    turn_idx: int = 1
    win: bool = False
    while turn_idx <= 5 and win == False:
        print(f"=== Turn {turn_idx}/5 ===")
        row_guess: int = input_guess(grid_size, "row")
        column_guess: int = input_guess(grid_size, "column")
        correct = correct_guess(secret_column, secret_column, row_guess, column_guess)
        print_grid(grid_size, row_guess, column_guess, correct)
        if row_guess == secret_row and column_guess == secret_column:
            print("Hit!")
            print(f"You won in {turn_idx}/5 turns!")
            win: bool = True
        else:
            print("Miss!")
        turn_idx += 1
    if turn_idx > 5:
        print(f"{turn_idx}/6 - Better luck next time!")

if __name__ == "__main__":
        grid_size: int = random.randint(3, 5)
        main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))