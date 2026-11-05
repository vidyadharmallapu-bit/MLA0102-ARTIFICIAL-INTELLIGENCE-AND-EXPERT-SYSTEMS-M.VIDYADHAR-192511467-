"""Hill Climbing Demo

Beginner-friendly version.
This file uses simple Python loops, lists, and dictionaries.
No heavy libraries or advanced tricks are used.
"""



def function_value(x):
    return -(x - 3) ** 2 + 10


def hill_climb(start, step_size, steps):
    current = start
    best = function_value(current)

    for _ in range(steps):
        candidates = [current - step_size, current + step_size]
        values = [function_value(c) for c in candidates]
        next_point = candidates[values.index(max(values))]
        next_value = max(values)

        if next_value <= best:
            break

        current = next_point
        best = next_value

    return current, best


def main():
    x, value = hill_climb(0, 0.5, 10)
    print('Best point found:', x)
    print('Best value:', value)


if __name__ == "__main__":
    main()
