"""Iterative Deepening DFS Demo

Beginner-friendly version.
This file uses simple Python loops, lists, and dictionaries.
No heavy libraries or advanced tricks are used.
"""



def dls(graph, node, goal, depth, path):
    if node == goal:
        return path
    if depth == 0:
        return None

    for neighbor in graph.get(node, []):
        if neighbor in path:
            continue
        answer = dls(graph, neighbor, goal, depth - 1, path + [neighbor])
        if answer is not None:
            return answer
    return None


def iddfs(graph, start, goal):
    for depth in range(len(graph) + 1):
        path = dls(graph, start, goal, depth, [start])
        if path is not None:
            return path
    return None


def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': ['H'],
        'E': [],
        'F': [],
        'G': [],
        'H': []
    }

    result = iddfs(graph, 'A', 'G')
    if result:
        print('Path found:', ' -> '.join(result))
    else:
        print('No path found.')


if __name__ == "__main__":
    main()
