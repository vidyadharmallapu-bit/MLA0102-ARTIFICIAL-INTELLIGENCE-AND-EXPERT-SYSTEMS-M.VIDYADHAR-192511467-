"""Solve a small 0/1 knapsack instance with a genetic algorithm."""

import random

ITEMS = [(2, 6), (3, 5), (5, 10), (4, 7), (1, 3), (6, 12)]
CAPACITY = 10


def fitness(chromosome):
    weight = sum(gene * item[0] for gene, item in zip(chromosome, ITEMS))
    value = sum(gene * item[1] for gene, item in zip(chromosome, ITEMS))
    return value if weight <= CAPACITY else 0


def crossover(first, second, rng):
    point = rng.randrange(1, len(ITEMS))
    return first[:point] + second[point:], second[:point] + first[point:]


def genetic_search(seed=7, population_size=40, generations=100):
    rng = random.Random(seed)
    population = [tuple(rng.randrange(2) for _ in ITEMS) for _ in range(population_size)]
    for _ in range(generations):
        population.sort(key=fitness, reverse=True)
        next_population = population[:2]
        while len(next_population) < population_size:
            first, second = rng.choices(population[:population_size // 2], k=2)
            child, _ = crossover(first, second, rng)
            child = tuple(1 - gene if rng.random() < 0.05 else gene for gene in child)
            next_population.append(child)
        population = next_population
    return max(population, key=fitness)


def main():
    chosen = genetic_search()
    selected = [(index + 1, *item) for index, (gene, item) in enumerate(zip(chosen, ITEMS)) if gene]
    print(f"Capacity: {CAPACITY}")
    print("Selected items (number, weight, value):", selected)
    print("Total weight:", sum(weight for _, weight, _ in selected))
    print("Maximum fitness value:", fitness(chosen))


if __name__ == "__main__":
    main()