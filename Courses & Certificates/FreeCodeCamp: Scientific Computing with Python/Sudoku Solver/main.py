from typing import Generator
import Sudoku_solver
import os


def solve_sudoku(board) -> Sudoku_solver.Sudoku_solver:
    gameboard = Sudoku_solver.Sudoku_solver(board)
    print(f"Puzzle to solve:\n{gameboard}")
    input("\nPress enter to solve...")
    os.system("clear")
    if gameboard.solver():
        os.system("clear")
        print(f"Solved puzzle:\n{gameboard}")
    else:
        print("The provided puzzle is unsolvable.")
    return gameboard


def load_puzzle(difficulty):
    match difficulty:
        case 1:
            file_name = "easy.txt"
        case 2:
            file_name = "medium.txt"
        case 3:
            file_name = "hard.txt"

    directory = f"examples/{file_name}"

    puzzle = []
    with open(directory, "r") as text_file:
        for line in text_file:
            puzzle.append(list(map(int, line.split())))

    return puzzle


print("-----Sudoku Resolver-----\n1. Easy\n2. Medium\n3. Hard\n")
while True:
    try:
        difficulty = input("Type your choice: ")

        if not difficulty.isdigit() or int(difficulty) < 1 or int(difficulty) > 3:
            raise ValueError("Please type a valid choice between 1 and 3")

        puzzle = load_puzzle(int(difficulty))
        solve_sudoku(puzzle)
        break

    except ValueError as e:
        print(e)
    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
