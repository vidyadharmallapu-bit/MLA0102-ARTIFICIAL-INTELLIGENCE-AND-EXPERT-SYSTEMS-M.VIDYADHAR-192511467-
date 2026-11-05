"""Greedy best-first search using node heuristic values."""

import heapq
from itertools import count

GRAPH = {
    "A": [("B", 2), ("C", 1)],
    "B": [("D", 3), ("E", 1)],
    "C": [("F", 2)],
    "D": [("G", 2)],
    "E": [("G", 5)],
    "F": [("G", 2)],
    "G": [],
}
HEURISTIC = {"A": 7, "B": 5, "C": 4, "D": 2, "E": 3, "F": 1, "G": 0}


def greedy_best_first(graph, heuristic, start, goal):
    serial = count()
    frontier = [(heuristic[start], next(serial), start)]
    parent = {start: None}
    visited = set()
    while frontier:
        _, _, node = heapq.heappop(frontier)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]
        for neighbor, _ in graph.get(node, []):
            if neighbor not in parent:
                parent[neighbor] = node
                heapq.heappush(frontier, (heuristic[neighbor], next(serial), neighbor))
    return None


def main():
    path = greedy_best_first(GRAPH, HEURISTIC, "A", "G")
    print("Path:", " -> ".join(path) if path else "No path found")
    print("Weighted path cost:", sum(next(cost for neighbor, cost in GRAPH[a] if neighbor == b)
                                      for a, b in zip(path, path[1:])))


if __name__ == "__main__":
    main()