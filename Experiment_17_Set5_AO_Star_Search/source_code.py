"""Solve a finite acyclic AND-OR graph using AO* cost evaluation."""

OPTIONS = {
    "A": [["B", "C"], ["D"]],
    "B": [["E"], ["F"]],
    "C": [["G"]],
    "D": [["H", "I"]],
    "E": [], "F": [], "G": [], "H": [], "I": [],
}
EDGE_COST = {
    ("A", "B"): 1, ("A", "C"): 1, ("A", "D"): 2,
    ("B", "E"): 2, ("B", "F"): 1, ("C", "G"): 2,
    ("D", "H"): 1, ("D", "I"): 1,
}
TERMINAL_COST = {"E": 5, "F": 1, "G": 2, "H": 2, "I": 2}


def ao_star(start):
    chosen, memo, active = {}, {}, set()

    def evaluate(node):
        if node in memo:
            return memo[node]
        if node in active:
            raise ValueError("AO* example graph must not contain cycles")
        alternatives = OPTIONS[node]
        if not alternatives:
            return TERMINAL_COST[node]
        active.add(node)
        costs = [
            sum(EDGE_COST[(node, child)] + evaluate(child) for child in children)
            for children in alternatives
        ]
        active.remove(node)
        best_index = min(range(len(costs)), key=costs.__getitem__)
        chosen[node] = alternatives[best_index]
        memo[node] = costs[best_index]
        return memo[node]

    total = evaluate(start)
    return total, chosen


def display_solution(node, chosen, indent=""):
    print(f"{indent}{node}")
    for child in chosen.get(node, []):
        display_solution(child, chosen, indent + "  ")


def main():
    cost, solution = ao_star("A")
    print(f"Minimum solution cost: {cost}")
    print("Selected solution graph:")
    display_solution("A", solution)


if __name__ == "__main__":
    main()