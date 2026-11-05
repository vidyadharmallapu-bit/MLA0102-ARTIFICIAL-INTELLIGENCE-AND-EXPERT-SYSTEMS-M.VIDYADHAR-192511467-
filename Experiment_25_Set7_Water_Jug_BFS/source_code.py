"""Use BFS to measure exactly four litres with 5L and 3L jugs."""

from collections import deque

CAPACITIES = (5, 3)


def successors(state):
    first, second = state
    actions = [
        ("Fill 5L jug", (5, second)),
        ("Fill 3L jug", (first, 3)),
        ("Empty 5L jug", (0, second)),
        ("Empty 3L jug", (first, 0)),
    ]
    transfer = min(first, CAPACITIES[1] - second)
    actions.append(("Pour 5L -> 3L", (first - transfer, second + transfer)))
    transfer = min(second, CAPACITIES[0] - first)
    actions.append(("Pour 3L -> 5L", (first + transfer, second - transfer)))
    return [(action, next_state) for action, next_state in actions if next_state != state]


def solve():
    start = (0, 0)
    queue = deque([start])
    parent = {start: None}
    action_taken = {}
    goal = None
    while queue:
        state = queue.popleft()
        if 4 in state:
            goal = state
            break
        for action, next_state in successors(state):
            if next_state not in parent:
                parent[next_state] = state
                action_taken[next_state] = action
                queue.append(next_state)
    if goal is None:
        return None
    path = []
    while goal is not None:
        path.append((goal, action_taken.get(goal)))
        goal = parent[goal]
    return list(reversed(path))


def main():
    path = solve()
    if path is None:
        print("No solution found.")
        return
    for step, (state, action) in enumerate(path):
        label = "Start" if step == 0 else action
        print(f"{step}: {label:18} -> 5L={state[0]}L, 3L={state[1]}L")


if __name__ == "__main__":
    main()