"""8 Puzzle Demo

Beginner-friendly version.
This file uses simple Python loops, lists, and dictionaries.
No heavy libraries or advanced tricks are used.
"""



def is_goal(state, goal):
    return state == goal


def possible_moves(state):
    zero = state.index(0)
    row, col = divmod(zero, 3)
    moves = []

    if row > 0:
        moves.append('up')
    if row < 2:
        moves.append('down')
    if col > 0:
        moves.append('left')
    if col < 2:
        moves.append('right')
    return moves


def move_blank(state, direction):
    zero = state.index(0)
    row, col = divmod(zero, 3)
    new_state = list(state)

    if direction == 'up':
        swap_index = zero - 3
    elif direction == 'down':
        swap_index = zero + 3
    elif direction == 'left':
        swap_index = zero - 1
    elif direction == 'right':
        swap_index = zero + 1
    else:
        return state

    new_state[zero], new_state[swap_index] = new_state[swap_index], new_state[zero]
    return tuple(new_state)


def main():
    start = (1, 2, 3, 4, 0, 5, 7, 8, 6)
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    print('Start state:', start)
    print('Goal state:', goal)
    print('Possible moves from the blank tile:', possible_moves(start))
    print('One sample move: ', move_blank(start, 'right'))


if __name__ == "__main__":
    main()
