"""Solve a 9x9 Sudoku CSP using backtracking and minimum remaining values."""

PUZZLE = [
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


def candidates(board, row, column):
    used = set(board[row])
    used.update(board[r][column] for r in range(9))
    box_row, box_column = row // 3 * 3, column // 3 * 3
    used.update(board[r][c] for r in range(box_row, box_row + 3)
                for c in range(box_column, box_column + 3))
    return [value for value in range(1, 10) if value not in used]


def solve(board):
    empty_cells = [
        (len(options), row, column, options)
        for row in range(9) for column in range(9)
        if board[row][column] == 0
        for options in [candidates(board, row, column)]
    ]
    if not empty_cells:
        return True
    _, row, column, options = min(empty_cells)
    for value in options:
        board[row][column] = value
        if solve(board):
            return True
        board[row][column] = 0
    return False


def main():
    board = [row.copy() for row in PUZZLE]
    if not solve(board):
        print("The supplied Sudoku has no solution.")
        return
    print("Solved Sudoku:")
    for row in board:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main()