"""Approximate a shortest TSP tour with a permutation genetic algorithm."""

import math
import random

CITIES = {
    "A": (0, 0), "B": (2, 6), "C": (5, 3), "D": (6, 7),
    "E": (8, 2), "F": (1, 4),
}


def tour_length(tour):
    route = tour + (tour[0],)
    return sum(math.dist(CITIES[first], CITIES[second]) for first, second in zip(route, route[1:]))


def ordered_crossover(first, second, rng):
    left, right = sorted(rng.sample(range(len(first)), 2))
    child = [None] * len(first)
    child[left:right] = first[left:right]
    remaining = [city for city in second if city not in child]
    positions = list(range(right, len(first))) + list(range(left))
    for position, city in zip(positions, remaining):
        child[position] = city
    return tuple(child)


def genetic_tsp(seed=19, population_size=60, generations=250):
    rng = random.Random(seed)
    cities = tuple(CITIES)
    population = [tuple(rng.sample(cities, len(cities))) for _ in range(population_size)]
    for _ in range(generations):
        population.sort(key=tour_length)
        next_population = population[:2]
        while len(next_population) < population_size:
            parent_a, parent_b = rng.choices(population[:population_size // 2], k=2)
            child = ordered_crossover(parent_a, parent_b, rng)
            if rng.random() < 0.2:
                first, second = rng.sample(range(len(child)), 2)
                mutable = list(child)
                mutable[first], mutable[second] = mutable[second], mutable[first]
                child = tuple(mutable)
            next_population.append(child)
        population = next_population
    return min(population, key=tour_length)


def main():
    route = genetic_tsp()
    print("Shortest route found:", " -> ".join(route + (route[0],)))
    print(f"Route length: {tour_length(route):.2f}")


if __name__ == "__main__":
    main()