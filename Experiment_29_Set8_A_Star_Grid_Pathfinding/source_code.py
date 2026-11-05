"""Find a shortest 4-directional path around grid obstacles using A*."""

import heapq
from itertools import count

ROWS, COLUMNS = 7, 9
START, GOAL = (0, 0), (6, 8)
OBSTACLES = {
    (1, 1), (1, 2), (1, 3), (2, 3), (3, 3),
    (4, 5), (4, 6), (4, 7), (5, 1), (5, 7),
}


def heuristic(position):
    return abs(position[0] - GOAL[0]) + abs(position[1] - GOAL[1])


def astar():
    serial = count()
    frontier = [(heuristic(START), 0, next(serial), START)]
    parent, cost = {START: None}, {START: 0}
    while frontier:
        _, current_cost, _, current = heapq.heappop(frontier)
        if current_cost != cost[current]:
            continue
        if current == GOAL:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]
        row, column = current
        for neighbor in ((row - 1, column), (row + 1, column),
                         (row, column - 1), (row, column + 1)):
            r, c = neighbor
            if not (0 <= r < ROWS and 0 <= c < COLUMNS) or neighbor in OBSTACLES:
                continue
            new_cost = current_cost + 1
            if new_cost < cost.get(neighbor, float("inf")):
                cost[neighbor] = new_cost
                parent[neighbor] = current
                heapq.heappush(frontier, (new_cost + heuristic(neighbor), new_cost,
                                          next(serial), neighbor))
    return None


def main():
    path = astar()
    path_set = set(path or [])
    for row in range(ROWS):
        print(" ".join("S" if (row, col) == START else "G" if (row, col) == GOAL
                         else "#" if (row, col) in OBSTACLES
                         else "*" if (row, col) in path_set else "."
                         for col in range(COLUMNS)))
    print("Path length:", len(path) - 1 if path else "No path found")
    if path:
        print("Path:", " -> ".join(map(str, path)))


if __name__ == "__main__":
    main()