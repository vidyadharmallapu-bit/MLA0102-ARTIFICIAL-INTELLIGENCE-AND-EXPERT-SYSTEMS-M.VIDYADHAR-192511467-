"""Genetic Algorithm Demo

Beginner-friendly version.
This file uses simple Python loops, lists, and dictionaries.
No heavy libraries or advanced tricks are used.
"""



import random


def fitness(chromosome):
    return sum(chromosome)


def main():
    random.seed(1)
    population = [
        [random.randint(0, 1) for _ in range(6)]
        for _ in range(10)
    ]

    for _ in range(10):
        population.sort(key=fitness, reverse=True)
        best = population[0]
        print('Best chromosome:', best, 'Fitness:', fitness(best))

        new_population = [best]
        while len(new_population) < len(population):
            parent1 = random.choice(population[:5])
            parent2 = random.choice(population[:5])
            child = parent1[:3] + parent2[3:]
            if random.random() < 0.1:
                child[random.randrange(len(child))] = 1 - child[random.randrange(len(child))]
            new_population.append(child)
        population = new_population


if __name__ == "__main__":
    main()
