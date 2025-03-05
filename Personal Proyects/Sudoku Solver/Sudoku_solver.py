import os
import time

class Sudoku_solver:
    def __init__(self, board) -> None:
        self.board = board

    def __str__(self) -> str:
        board_str = ""
        for row_index, row in enumerate(self.board):
            if row_index % 3 == 0 and row_index != 0:
                board_str += "------+-------+------\n"
            row_str = [str(i) if i else "*" for i in row]
            row_with_separators = " | ".join(
                [" ".join(row_str[i : i + 3]) for i in range(0, len(row_str), 3)]
            )
            board_str += row_with_separators + "\n"
        return board_str

    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None

    def valid_in_row(self, row, num) -> bool:
        return num not in self.board[row]

    def valid_in_col(self, col, num) -> bool:
        return all(self.board[row][col] != num for row in range(9))

    def valid_in_square(self, row, col, num) -> bool:
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty, num) -> bool:
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        return all([valid_in_row, valid_in_col, valid_in_square])

    def solver(self) -> bool:
        if (next_empty := self.find_empty_cell()) is None:
            return True
        for guess in range(1, 10):
            if self.is_valid(next_empty, guess):
                row, col = next_empty
                self.board[row][col] = guess
                os.system("clear")
                print(self)
                #time.sleep(0.1)
                if self.solver():
                    return True
                self.board[row][col] = 0
        return False
