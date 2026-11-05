"""Solve a 15-puzzle with A* and Manhattan-distance heuristic."""

import heapq
from itertools import count

SIZE = 4
START = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 14, 15)
GOAL = tuple(range(1, SIZE * SIZE)) + (0,)


def manhattan(state):
    total = 0
    for index, value in enumerate(state):
        if value:
            goal_index = value - 1
            row, column = divmod(index, SIZE)
            goal_row, goal_column = divmod(goal_index, SIZE)
            total += abs(row - goal_row) + abs(column - goal_column)
    return total


def solvable(state):
    tiles = [value for value in state if value]
    inversions = sum(first > second for index, first in enumerate(tiles)
                     for second in tiles[index + 1:])
    blank_row_from_bottom = SIZE - state.index(0) // SIZE
    return (inversions + blank_row_from_bottom) % 2 == 1


def neighbors(state):
    blank = state.index(0)
    row, column = divmod(blank, SIZE)
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        next_row, next_column = row + dr, column + dc
        if 0 <= next_row < SIZE and 0 <= next_column < SIZE:
            target = next_row * SIZE + next_column
            child = list(state)
            child[blank], child[target] = child[target], child[blank]
            yield tuple(child)


def astar(start):
    if not solvable(start):
        return None
    serial = count()
    frontier = [(manhattan(start), 0, next(serial), start)]
    parent, best_cost = {start: None}, {start: 0}
    while frontier:
        _, cost, _, state = heapq.heappop(frontier)
        if cost != best_cost[state]:
            continue
        if state == GOAL:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return path[::-1]
        for child in neighbors(state):
            new_cost = cost + 1
            if new_cost < best_cost.get(child, float("inf")):
                best_cost[child] = new_cost
                parent[child] = state
                heapq.heappush(frontier, (new_cost + manhattan(child), new_cost,
                                          next(serial), child))
    return None


def main():
    path = astar(START)
    if path is None:
        print("No solution exists for the selected board.")
        return
    print(f"Moves required: {len(path) - 1}")
    for step, state in enumerate(path):
        print(f"Step {step}:")
        for row in range(SIZE):
            print(" ".join("_" if value == 0 else f"{value:2}" 
                           for value in state[row * SIZE:(row + 1) * SIZE]))
        print()


if __name__ == "__main__":
    main()