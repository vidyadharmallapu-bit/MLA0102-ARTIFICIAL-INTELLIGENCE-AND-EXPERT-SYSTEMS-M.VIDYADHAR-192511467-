"""Solve 8-Queens with simulated annealing and display the final board."""

import math
import random

SIZE = 8


def conflicts(columns):
    return sum(
        columns[first] == columns[second]
        or abs(columns[first] - columns[second]) == second - first
        for first in range(SIZE)
        for second in range(first + 1, SIZE)
    )


def simulated_annealing(seed=42):
    rng = random.Random(seed)
    best = None
    for _ in range(100):
        current = rng.sample(range(SIZE), SIZE)
        energy = conflicts(current)
        temperature = 10.0
        while energy and temperature > 0.01:
            first, second = rng.sample(range(SIZE), 2)
            candidate = current.copy()
            candidate[first], candidate[second] = candidate[second], candidate[first]
            candidate_energy = conflicts(candidate)
            delta = candidate_energy - energy
            if delta < 0 or rng.random() < math.exp(-delta / temperature):
                current, energy = candidate, candidate_energy
            temperature *= 0.995
        if best is None or conflicts(current) < conflicts(best):
            best = current
        if energy == 0:
            return current
    return best


def main():
    columns = simulated_annealing()
    print("Final board (Q marks a queen):")
    for column in columns:
        print(" ".join("Q" if position == column else "." for position in range(SIZE)))
    print("Diagonal conflicts:", conflicts(columns))


if __name__ == "__main__":
    main()