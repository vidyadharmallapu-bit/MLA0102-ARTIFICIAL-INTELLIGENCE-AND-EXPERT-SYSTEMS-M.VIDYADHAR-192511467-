"""Solve the 3-missionaries, 3-cannibals river crossing with DFS."""

START = (3, 3, 0)  # missionaries left, cannibals left, boat: 0 left / 1 right
GOAL = (0, 0, 1)
BOAT_LOADS = ((2, 0), (0, 2), (1, 1), (1, 0), (0, 1))


def safe(missionaries, cannibals):
    return (missionaries == 0 or missionaries >= cannibals) and (
        3 - missionaries == 0 or 3 - missionaries >= 3 - cannibals
    )


def successors(state):
    missionaries, cannibals, boat = state
    direction = -1 if boat == 0 else 1
    for moved_m, moved_c in BOAT_LOADS:
        next_m = missionaries + direction * moved_m
        next_c = cannibals + direction * moved_c
        if 0 <= next_m <= 3 and 0 <= next_c <= 3 and safe(next_m, next_c):
            yield (next_m, next_c, 1 - boat)


def depth_first_search(state=START, path=None, visited=None):
    path = [state] if path is None else path
    visited = set() if visited is None else visited
    if state == GOAL:
        return path
    visited.add(state)
    for next_state in successors(state):
        if next_state not in visited:
            result = depth_first_search(next_state, path + [next_state], visited)
            if result:
                return result
    return None


def main():
    path = depth_first_search()
    if path is None:
        print("No solution found.")
        return
    for step, (missionaries, cannibals, boat) in enumerate(path):
        side = "left" if boat == 0 else "right"
        print(f"{step}: left=({missionaries}M,{cannibals}C), "
              f"right=({3-missionaries}M,{3-cannibals}C), boat={side}")


if __name__ == "__main__":
    main()