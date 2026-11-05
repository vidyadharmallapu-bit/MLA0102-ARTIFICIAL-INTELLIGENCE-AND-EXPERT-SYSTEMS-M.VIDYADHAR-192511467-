"""N-Queens Backtracking Demo

Beginner-friendly version.
This file uses simple Python loops, lists, and dictionaries.
No heavy libraries or advanced tricks are used.
"""



def is_safe(board, row, col):
    for r, c in enumerate(board[:row]):
        if c == col:
            return False
        if abs(r - row) == abs(c - col):
            return False
    return True


def solve_n_queens(n, row=0, board=None):
    if board is None:
        board = []
    if row == n:
        return board

    for col in range(n):
        if is_safe(board, row, col):
            board.append(col)
            result = solve_n_queens(n, row + 1, board)
            if result is not None:
                return result
            board.pop()
    return None


def main():
    n = 4
    result = solve_n_queens(n)
    if result:
        print('One valid solution:', result)
    else:
        print('No solution for this board size.')


if __name__ == "__main__":
    main()
