"""Solve an 8-puzzle with best-first search and misplaced-tile heuristic."""

import heapq
from itertools import count

START = (1, 2, 3, 4, 0, 6, 7, 5, 8)
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def misplaced_tiles(state, goal):
    return sum(value != 0 and value != goal[index] for index, value in enumerate(state))


def neighbors(state):
    blank = state.index(0)
    row, col = divmod(blank, 3)
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        next_row, next_col = row + dr, col + dc
        if 0 <= next_row < 3 and 0 <= next_col < 3:
            target = next_row * 3 + next_col
            child = list(state)
            child[blank], child[target] = child[target], child[blank]
            yield tuple(child)


def solve(start, goal):
    serial = count()
    frontier = [(misplaced_tiles(start, goal), 0, next(serial), start)]
    parent, best_cost = {start: None}, {start: 0}
    while frontier:
        _, cost, _, state = heapq.heappop(frontier)
        if cost != best_cost[state]:
            continue
        if state == goal:
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
                heapq.heappush(frontier, (misplaced_tiles(child, goal), new_cost, next(serial), child))
    return None


def main():
    path = solve(START, GOAL)
    if path is None:
        print("No solution found.")
        return
    print(f"Moves required: {len(path) - 1}")
    for step, state in enumerate(path):
        print(f"Step {step}:")
        for row in range(0, 9, 3):
            print(" ".join("_" if value == 0 else str(value) for value in state[row:row + 3]))
        print()


if __name__ == "__main__":
    main()