"""Depth-First Search Demo

Beginner-friendly version.
This file uses simple Python loops, lists, and dictionaries.
No heavy libraries or advanced tricks are used.
"""



def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = set()

    if start == goal:
        return [start]

    visited.add(start)

    for neighbor in graph.get(start, []):
        if neighbor in visited:
            continue

        result = dfs(graph, neighbor, goal, visited)
        if result is not None:
            return [start] + result

    return None


def main():
    graph = {
        'S': ['A', 'B'],
        'A': ['C'],
        'B': ['D'],
        'C': ['G'],
        'D': ['G'],
        'G': []
    }

    path = dfs(graph, 'S', 'G')
    if path:
        print('Path found:', ' -> '.join(path))
    else:
        print('No path found.')


if __name__ == "__main__":
    main()
