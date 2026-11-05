"""Greedy Best-First Search

Beginner-friendly version.
This file uses simple Python loops, lists, and dictionaries.
No heavy libraries or advanced tricks are used.
"""



def greedy_best_first(graph, start, goal, heuristic):
    frontier = [(heuristic[start], [start])]
    visited = set()

    while frontier:
        frontier.sort(key=lambda item: item[0])
        _, path = frontier.pop(0)
        node = path[-1]

        if node == goal:
            return path

        if node in visited:
            continue
        visited.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                frontier.append((heuristic[neighbor], path + [neighbor]))

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
    heuristic = {'S': 4, 'A': 2, 'B': 3, 'C': 1, 'D': 1, 'G': 0}

    answer = greedy_best_first(graph, 'S', 'G', heuristic)
    if answer:
        print('Best-first path:', ' -> '.join(answer))
    else:
        print('No path found.')


if __name__ == "__main__":
    main()
