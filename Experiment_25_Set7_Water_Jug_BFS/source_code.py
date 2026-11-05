"""Water Jug BFS Demo

Beginner-friendly version.
This file uses simple Python loops, lists, and dictionaries.
No heavy libraries or advanced tricks are used.
"""



def water_jug_steps(start, goal):
    visited = set()
    queue = [(start, [])]

    while queue:
        state, path = queue.pop(0)
        if state in visited:
            continue
        visited.add(state)

        if state == goal:
            return path + [state]

        a, b = state
        moves = [
            ((4, b), 'Fill A'),
            ((a, 3), 'Fill B'),
            ((0, b), 'Empty A'),
            ((a, 0), 'Empty B'),
            ((max(0, a - (3 - b)), min(3, b + a)), 'Pour A to B'),
            ((min(4, a + b), max(0, b - (4 - a))), 'Pour B to A')
        ]

        for new_state, action in moves:
            if new_state not in visited:
                queue.append((new_state, path + [(state, action, new_state)]))

    return None


def main():
    start = (0, 0)
    goal = (2, 0)
    answer = water_jug_steps(start, goal)
    if answer:
        print('Solution path:')
        for step in answer:
            print(step)
    else:
        print('No solution found.')


if __name__ == "__main__":
    main()
