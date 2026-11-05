"""Solve 8-Queens with a genetic algorithm and show its operators."""

import random

SIZE = 8
MAX_FITNESS = SIZE * (SIZE - 1) // 2


def conflicts(chromosome):
    return sum(chromosome[first] == chromosome[second]
               or abs(chromosome[first] - chromosome[second]) == second - first
               for first in range(SIZE) for second in range(first + 1, SIZE))


def fitness(chromosome):
    return MAX_FITNESS - conflicts(chromosome)


def crossover(first, second, rng, point=None):
    point = point or rng.randrange(1, SIZE)
    return first[:point] + second[point:]


def mutate(chromosome, rng):
    column = rng.randrange(SIZE)
    rows = [row for row in range(SIZE) if row != chromosome[column]]
    child = list(chromosome)
    child[column] = rng.choice(rows)
    return tuple(child)


def genetic_search(seed=34, population_size=120, generations=1500):
    rng = random.Random(seed)
    population = [tuple(rng.randrange(SIZE) for _ in range(SIZE))
                  for _ in range(population_size)]
    operations = None
    for _ in range(generations):
        population.sort(key=fitness, reverse=True)
        if fitness(population[0]) == MAX_FITNESS:
            return population[0], operations
        next_generation = population[:4]
        while len(next_generation) < population_size:
            parent_a, parent_b = rng.choices(population[:population_size // 2], k=2)
            if operations is None:
                crossed = crossover(parent_a, parent_b, rng, point=4)
                mutated = mutate(crossed, rng)
                operations = (parent_a, parent_b, crossed, mutated)
            else:
                crossed = crossover(parent_a, parent_b, rng)
                mutated = mutate(crossed, rng) if rng.random() < 0.2 else crossed
            next_generation.append(mutated)
        population = next_generation
    best = max(population, key=fitness)
    return best, operations


def main():
    solution, operations = genetic_search()
    if operations:
        parent_a, parent_b, crossed, mutated = operations
        print("Crossover parents:", parent_a, parent_b)
        print("After single-point crossover:", crossed)
        print("After mutation:", mutated)
    print("Best chromosome (row for each column):", solution)
    print(f"Fitness: {fitness(solution)}/{MAX_FITNESS}")
    for row in range(SIZE):
        print(" ".join("Q" if solution[column] == row else "."
                       for column in range(SIZE)))


if __name__ == "__main__":
    main()