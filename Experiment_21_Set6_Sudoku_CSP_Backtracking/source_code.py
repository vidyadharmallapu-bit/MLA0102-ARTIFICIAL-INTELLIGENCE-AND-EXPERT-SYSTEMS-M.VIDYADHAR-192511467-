"""Sudoku Backtracking Demo

Beginner-friendly version.
This file uses simple Python loops, lists, and dictionaries.
No heavy libraries or advanced tricks are used.
"""



def print_board(board):
    for row in board:
        print(row)


def is_valid(board, row, col, value):
    for c in range(9):
        if board[row][c] == value:
            return False
    for r in range(9):
        if board[r][col] == value:
            return False
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == value:
                return False
    return True


def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for value in range(1, 10):
                    if is_valid(board, row, col, value):
                        board[row][col] = value
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def main():
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    if solve(board):
        print('Solved board:')
        print_board(board)
    else:
        print('No solution found.')


if __name__ == "__main__":
    main()
