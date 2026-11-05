"""Bidirectional Search Demo

Beginner-friendly version.
This file uses simple Python loops, lists, and dictionaries.
No heavy libraries or advanced tricks are used.
"""



def bidirectional_search(graph, start, goal):
    front_start = [start]
    front_goal = [goal]
    visited_start = {start}
    visited_goal = {goal}

    while front_start and front_goal:
        for node in list(front_start):
            for neighbor in graph.get(node, []):
                if neighbor not in visited_start:
                    visited_start.add(neighbor)
                    front_start.append(neighbor)
                if neighbor in visited_goal:
                    return True

        for node in list(front_goal):
            for neighbor in graph.get(node, []):
                if neighbor not in visited_goal:
                    visited_goal.add(neighbor)
                    front_goal.append(neighbor)
                if neighbor in visited_start:
                    return True

    return False


def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': ['E'],
        'E': ['F'],
        'F': []
    }

    if bidirectional_search(graph, 'A', 'F'):
        print('A path exists between start and goal.')
    else:
        print('No path found.')


if __name__ == "__main__":
    main()
