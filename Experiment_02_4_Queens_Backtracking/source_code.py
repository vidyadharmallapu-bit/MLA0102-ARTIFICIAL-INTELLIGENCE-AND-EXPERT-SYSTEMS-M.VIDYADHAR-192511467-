"""Display every solution to the 4-Queens problem using backtracking."""


BOARD_SIZE = 4


def solve_queens(size):
    solutions = []
    queen_columns = []

    def place_queen(row, used_columns, descending_diagonals, ascending_diagonals):
        if row == size:
            solutions.append(queen_columns.copy())
            return

        for column in range(size):
            descending = row - column
            ascending = row + column
            if (
                column not in used_columns
                and descending not in descending_diagonals
                and ascending not in ascending_diagonals
            ):
                queen_columns.append(column)
                place_queen(
                    row + 1,
                    used_columns | {column},
                    descending_diagonals | {descending},
                    ascending_diagonals | {ascending},
                )
                queen_columns.pop()

    place_queen(0, set(), set(), set())
    return solutions


def display_solution(columns, number):
    print(f"Solution {number} (columns by row: {[column + 1 for column in columns]}):")
    for queen_column in columns:
        print(" ".join("Q" if column == queen_column else "." for column in range(BOARD_SIZE)))
    print()


def main():
    solutions = solve_queens(BOARD_SIZE)
    print(f"4-Queens solutions found: {len(solutions)}\n")
    for number, columns in enumerate(solutions, start=1):
        display_solution(columns, number)


if __name__ == "__main__":
    main()