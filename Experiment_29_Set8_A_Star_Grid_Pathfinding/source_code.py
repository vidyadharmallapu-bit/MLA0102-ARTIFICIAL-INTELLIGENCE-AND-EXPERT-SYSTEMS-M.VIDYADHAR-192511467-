"""A* Search Demo

Beginner-friendly version.
This file uses simple Python loops, lists, and dictionaries.
No heavy libraries or advanced tricks are used.
"""



def a_star(graph, start, goal, heuristic):
    open_list = [(heuristic[start], 0, [start])]
    visited = {}

    while open_list:
        open_list.sort()
        _, cost, path = open_list.pop(0)
        node = path[-1]

        if node == goal:
            return path, cost

        for neighbor in graph.get(node, []):
            new_cost = cost + graph[node][neighbor]
            new_path = path + [neighbor]
            f_value = new_cost + heuristic[neighbor]
            if neighbor not in visited or new_cost < visited[neighbor]:
                visited[neighbor] = new_cost
                open_list.append((f_value, new_cost, new_path))

    return None, None


def main():
    graph = {
        'S': {'A': 2, 'B': 5},
        'A': {'C': 4},
        'B': {'C': 1},
        'C': {'G': 3},
        'G': {}
    }
    heuristic = {'S': 5, 'A': 3, 'B': 4, 'C': 2, 'G': 0}

    path, cost = a_star(graph, 'S', 'G', heuristic)
    if path:
        print('Path:', ' -> '.join(path), 'Cost:', cost)
    else:
        print('No path found.')


if __name__ == "__main__":
    main()
