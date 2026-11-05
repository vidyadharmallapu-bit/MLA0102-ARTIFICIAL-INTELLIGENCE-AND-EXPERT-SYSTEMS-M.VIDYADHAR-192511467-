"""Maximize a one-dimensional function with simple hill climbing."""


def objective(x):
    return -(x - 3) ** 2 + 9


def hill_climb(start, minimum, maximum):
    current = start
    visited = [current]
    while True:
        candidates = [x for x in (current - 1, current + 1) if minimum <= x <= maximum]
        best = max(candidates, key=objective, default=current)
        if objective(best) <= objective(current):
            return visited
        current = best
        visited.append(current)


def main():
    visited = hill_climb(start=-2, minimum=-5, maximum=8)
    print("Function: f(x) = -(x - 3)^2 + 9")
    print("States visited (x, f(x)):")
    for x in visited:
        print(f"({x}, {objective(x)})")
    print(f"Maximum found: f({visited[-1]}) = {objective(visited[-1])}")


if __name__ == "__main__":
    main()