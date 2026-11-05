"""Bidirectional breadth-first search on an undirected graph."""

from collections import deque

GRAPH = {
    "A": ["B", "C"], "B": ["A", "D", "E"], "C": ["A", "F"],
    "D": ["B", "G"], "E": ["B", "G"], "F": ["C", "G"],
    "G": ["D", "E", "F"],
}


def expand_layer(queue, parents, other_parents, graph):
    for _ in range(len(queue)):
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in parents:
                parents[neighbor] = node
                queue.append(neighbor)
            if neighbor in other_parents:
                return neighbor
    return None


def bidirectional_search(graph, start, goal):
    if start not in graph or goal not in graph:
        return None
    if start == goal:
        return [start]
    forward_queue, backward_queue = deque([start]), deque([goal])
    forward, backward = {start: None}, {goal: None}
    while forward_queue and backward_queue:
        if len(forward_queue) <= len(backward_queue):
            meeting = expand_layer(forward_queue, forward, backward, graph)
        else:
            meeting = expand_layer(backward_queue, backward, forward, graph)
        if meeting is not None:
            left, node = [], meeting
            while node is not None:
                left.append(node)
                node = forward[node]
            left.reverse()
            node = backward[meeting]
            while node is not None:
                left.append(node)
                node = backward[node]
            return left
    return None


def main():
    path = bidirectional_search(GRAPH, "A", "G")
    print("Graph:", GRAPH)
    print("Path:", " -> ".join(path) if path else "No path found")


if __name__ == "__main__":
    main()