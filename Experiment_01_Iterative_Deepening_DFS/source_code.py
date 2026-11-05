"""Find a goal in a state-space graph using iterative deepening DFS."""


GRAPH = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["H"],
    "E": [],
    "F": [],
    "G": [],
    "H": [],
}


def depth_limited_search(graph, current, goal, remaining_depth, path):
    if current == goal:
        return path
    if remaining_depth == 0:
        return None

    for neighbor in graph.get(current, []):
        if neighbor not in path:
            result = depth_limited_search(
                graph, neighbor, goal, remaining_depth - 1, path + [neighbor]
            )
            if result is not None:
                return result
    return None


def iterative_deepening_search(graph, start, goal):
    if start not in graph or goal not in graph:
        return None

    for depth_limit in range(len(graph)):
        result = depth_limited_search(graph, start, goal, depth_limit, [start])
        if result is not None:
            return result
    return None


def main():
    print("State-space graph:")
    for node, neighbors in GRAPH.items():
        print(f"  {node}: {', '.join(neighbors) if neighbors else '(no children)'}")

    start = input("Enter the initial node [A]: ").strip().upper() or "A"
    goal = input("Enter the goal node [G]: ").strip().upper() or "G"

    if start not in GRAPH or goal not in GRAPH:
        print("Error: both nodes must exist in the displayed graph.")
        return

    path = iterative_deepening_search(GRAPH, start, goal)
    if path:
        print("Path:", " -> ".join(path))
    else:
        print(f"No path found from {start} to {goal}.")


if __name__ == "__main__":
    main()