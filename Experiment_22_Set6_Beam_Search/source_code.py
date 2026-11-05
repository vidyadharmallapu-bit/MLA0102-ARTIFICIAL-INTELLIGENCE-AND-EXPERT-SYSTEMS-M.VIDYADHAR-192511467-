"""Find a path with beam search, keeping only the best k nodes per layer."""

GRAPH = {
    "A": ["B", "C"], "B": ["D", "E"], "C": ["F", "G"],
    "D": ["H"], "E": ["H"], "F": ["G", "H"], "G": ["H"], "H": [],
}
HEURISTIC = {"A": 7, "B": 6, "C": 4, "D": 5, "E": 2, "F": 3, "G": 1, "H": 0}


def beam_search(graph, heuristic, start, goal, width):
    beam = [(start, [start])]
    visited = {start}
    while beam:
        for node, path in beam:
            if node == goal:
                return path
        candidates = {}
        for node, path in beam:
            for child in graph.get(node, []):
                if child not in visited:
                    candidates.setdefault(child, path + [child])
        if not candidates:
            break
        beam = sorted(candidates.items(), key=lambda item: heuristic[item[0]])[:width]
        visited.update(node for node, _ in beam)
    return None


def main():
    width = 2
    path = beam_search(GRAPH, HEURISTIC, "A", "H", width)
    print(f"Beam width: {width}")
    print("Best path:", " -> ".join(path) if path else "No path found")


if __name__ == "__main__":
    main()