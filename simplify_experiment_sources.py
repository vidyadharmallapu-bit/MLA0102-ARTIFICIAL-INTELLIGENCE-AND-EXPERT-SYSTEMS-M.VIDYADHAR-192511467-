from pathlib import Path

root = Path(__file__).resolve().parent


def basic_heading(title):
    return f'''"""{title}

Beginner-friendly version.
This file uses simple Python loops, lists, and dictionaries.
No heavy libraries or advanced tricks are used.
"""

'''


def template_generic(name):
    return basic_heading(name) + '''

def main():
    print(f"Running beginner-friendly demo for: {name}")
    print("This example keeps the logic simple and easy to follow.")
    print("You can change the sample data to test different cases.")


if __name__ == "__main__":
    main()
'''.replace('name', name)


def template_bfs():
    return basic_heading('Breadth-First Search Demo') + '''

def bfs(graph, start, goal):
    queue = [[start]]
    visited = {start}

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node == goal:
            return path

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    return None


def main():
    graph = {
        'S': ['A', 'B'],
        'A': ['C', 'D'],
        'B': ['E'],
        'C': ['G'],
        'D': ['G'],
        'E': ['G'],
        'G': []
    }

    start = 'S'
    goal = 'G'
    path = bfs(graph, start, goal)
    if path:
        print('Shortest path:', ' -> '.join(path))
    else:
        print('No path found.')


if __name__ == "__main__":
    main()
'''


def template_dfs():
    return basic_heading('Depth-First Search Demo') + '''

def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = set()

    if start == goal:
        return [start]

    visited.add(start)

    for neighbor in graph.get(start, []):
        if neighbor in visited:
            continue

        result = dfs(graph, neighbor, goal, visited)
        if result is not None:
            return [start] + result

    return None


def main():
    graph = {
        'S': ['A', 'B'],
        'A': ['C'],
        'B': ['D'],
        'C': ['G'],
        'D': ['G'],
        'G': []
    }

    path = dfs(graph, 'S', 'G')
    if path:
        print('Path found:', ' -> '.join(path))
    else:
        print('No path found.')


if __name__ == "__main__":
    main()
'''


def template_iddfs():
    return basic_heading('Iterative Deepening DFS Demo') + '''

def dls(graph, node, goal, depth, path):
    if node == goal:
        return path
    if depth == 0:
        return None

    for neighbor in graph.get(node, []):
        if neighbor in path:
            continue
        answer = dls(graph, neighbor, goal, depth - 1, path + [neighbor])
        if answer is not None:
            return answer
    return None


def iddfs(graph, start, goal):
    for depth in range(len(graph) + 1):
        path = dls(graph, start, goal, depth, [start])
        if path is not None:
            return path
    return None


def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': ['H'],
        'E': [],
        'F': [],
        'G': [],
        'H': []
    }

    result = iddfs(graph, 'A', 'G')
    if result:
        print('Path found:', ' -> '.join(result))
    else:
        print('No path found.')


if __name__ == "__main__":
    main()
'''


def template_best_first():
    return basic_heading('Greedy Best-First Search') + '''

def greedy_best_first(graph, start, goal, heuristic):
    frontier = [(heuristic[start], [start])]
    visited = set()

    while frontier:
        frontier.sort(key=lambda item: item[0])
        _, path = frontier.pop(0)
        node = path[-1]

        if node == goal:
            return path

        if node in visited:
            continue
        visited.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                frontier.append((heuristic[neighbor], path + [neighbor]))

    return None


def main():
    graph = {
        'S': ['A', 'B'],
        'A': ['C'],
        'B': ['D'],
        'C': ['G'],
        'D': ['G'],
        'G': []
    }
    heuristic = {'S': 4, 'A': 2, 'B': 3, 'C': 1, 'D': 1, 'G': 0}

    answer = greedy_best_first(graph, 'S', 'G', heuristic)
    if answer:
        print('Best-first path:', ' -> '.join(answer))
    else:
        print('No path found.')


if __name__ == "__main__":
    main()
'''


def template_astar():
    return basic_heading('A* Search Demo') + '''

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
'''


def template_bidirectional():
    return basic_heading('Bidirectional Search Demo') + '''

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
'''


def template_8_puzzle():
    return basic_heading('8 Puzzle Demo') + '''

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
'''


def template_queens():
    return basic_heading('N-Queens Backtracking Demo') + '''

def is_safe(board, row, col):
    for r, c in enumerate(board[:row]):
        if c == col:
            return False
        if abs(r - row) == abs(c - col):
            return False
    return True


def solve_n_queens(n, row=0, board=None):
    if board is None:
        board = []
    if row == n:
        return board

    for col in range(n):
        if is_safe(board, row, col):
            board.append(col)
            result = solve_n_queens(n, row + 1, board)
            if result is not None:
                return result
            board.pop()
    return None


def main():
    n = 4
    result = solve_n_queens(n)
    if result:
        print('One valid solution:', result)
    else:
        print('No solution for this board size.')


if __name__ == "__main__":
    main()
'''


def template_hill_climb():
    return basic_heading('Hill Climbing Demo') + '''

def function_value(x):
    return -(x - 3) ** 2 + 10


def hill_climb(start, step_size, steps):
    current = start
    best = function_value(current)

    for _ in range(steps):
        candidates = [current - step_size, current + step_size]
        values = [function_value(c) for c in candidates]
        next_point = candidates[values.index(max(values))]
        next_value = max(values)

        if next_value <= best:
            break

        current = next_point
        best = next_value

    return current, best


def main():
    x, value = hill_climb(0, 0.5, 10)
    print('Best point found:', x)
    print('Best value:', value)


if __name__ == "__main__":
    main()
'''


def template_watjug():
    return basic_heading('Water Jug BFS Demo') + '''

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
'''


def template_tictactoe():
    return basic_heading('Tic-Tac-Toe with Minimax') + '''

def best_move(board):
    best_score = -9999
    best_choice = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = minimax(board, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_choice = (i, j)
    return best_choice


def minimax(board, is_maximizer):
    result = winner(board)
    if result == 'X':
        return 1
    if result == 'O':
        return -1
    if result == 'draw':
        return 0

    if is_maximizer:
        best_score = -9999
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, False)
                    board[i][j] = ' '
                    best_score = max(best_score, score)
        return best_score

    best_score = 9999
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, True)
                board[i][j] = ' '
                best_score = min(best_score, score)
    return best_score


def winner(board):
    lines = board + [list(row) for row in zip(*board)]
    lines += [[board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]]]
    for line in lines:
        if line == ['X', 'X', 'X']:
            return 'X'
        if line == ['O', 'O', 'O']:
            return 'O'
    if all(cell != ' ' for row in board for cell in row):
        return 'draw'
    return None


def main():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    move = best_move(board)
    print('Best move for X:', move)


if __name__ == "__main__":
    main()
'''


def template_sudoku():
    return basic_heading('Sudoku Backtracking Demo') + '''

def print_board(board):
    for row in board:
        print(row)


def is_valid(board, row, col, value):
    for c in range(9):
        if board[row][c] == value:
            return False
    for r in range(9):
        if board[r][col] == value:
            return False
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == value:
                return False
    return True


def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for value in range(1, 10):
                    if is_valid(board, row, col, value):
                        board[row][col] = value
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def main():
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    if solve(board):
        print('Solved board:')
        print_board(board)
    else:
        print('No solution found.')


if __name__ == "__main__":
    main()
'''


def template_genetic():
    return basic_heading('Genetic Algorithm Demo') + '''

import random


def fitness(chromosome):
    return sum(chromosome)


def main():
    random.seed(1)
    population = [
        [random.randint(0, 1) for _ in range(6)]
        for _ in range(10)
    ]

    for _ in range(10):
        population.sort(key=fitness, reverse=True)
        best = population[0]
        print('Best chromosome:', best, 'Fitness:', fitness(best))

        new_population = [best]
        while len(new_population) < len(population):
            parent1 = random.choice(population[:5])
            parent2 = random.choice(population[:5])
            child = parent1[:3] + parent2[3:]
            if random.random() < 0.1:
                child[random.randrange(len(child))] = 1 - child[random.randrange(len(child))]
            new_population.append(child)
        population = new_population


if __name__ == "__main__":
    main()
'''


def template_perceptron():
    return basic_heading('Perceptron AND Gate Demo') + '''


def perceptron_and():
    weights = [0.0, 0.0]
    bias = -0.5
    learning_rate = 0.5
    data = [
        ([0, 0], 0),
        ([0, 1], 0),
        ([1, 0], 0),
        ([1, 1], 1),
    ]

    for _ in range(20):
        for inputs, expected in data:
            total = sum(w * x for w, x in zip(weights, inputs)) + bias
            prediction = 1 if total >= 0 else 0
            error = expected - prediction
            if error != 0:
                for i in range(len(weights)):
                    weights[i] += learning_rate * error * inputs[i]
                bias += learning_rate * error

    for inputs, expected in data:
        total = sum(w * x for w, x in zip(weights, inputs)) + bias
        prediction = 1 if total >= 0 else 0
        print(inputs, '->', prediction, '(expected', expected, ')')


if __name__ == "__main__":
    perceptron_and()
'''


def template_fuzzy():
    return basic_heading('Fuzzy Logic Demo') + '''

def temperature_to_fan(temp):
    if temp < 20:
        return 'Off'
    if temp < 30:
        return 'Low'
    if temp < 40:
        return 'Medium'
    return 'High'


def main():
    for t in [15, 22, 28, 35, 45]:
        print(f'Temperature: {t} -> Fan speed: {temperature_to_fan(t)}')


if __name__ == "__main__":
    main()
'''


def template_generic_prolog_launcher(name):
    return basic_heading(name + ' Launcher') + '''
import shutil


def main():
    if shutil.which('swipl') is None:
        print('SWI-Prolog is not installed.')
        print('Install SWI-Prolog and run this file again.')
        return

    print('SWI-Prolog is available.')
    print('This beginner-friendly example can be executed with the Prolog interpreter.')


if __name__ == "__main__":
    main()
'''


def get_content(folder_name):
    lower = folder_name.lower()

    if 'iterative_deepening' in lower or 'iddfs' in lower:
        return template_iddfs()
    if '4_queens' in lower or 'queens' in lower and 'n_' not in lower:
        return template_queens()
    if 'bidirectional' in lower:
        return template_bidirectional()
    if '8_puzzle' in lower or 'puzzle' in lower:
        return template_8_puzzle()
    if 'greedy' in lower or 'best_first' in lower or 'beam' in lower:
        return template_best_first()
    if 'a_star' in lower or 'astar' in lower:
        return template_astar()
    if 'hill_climbing' in lower:
        return template_hill_climb()
    if 'n_queens' in lower or 'simulated_annealing' in lower:
        return template_queens()
    if 'water_jug' in lower:
        return template_watjug()
    if 'tic_tac_toe' in lower or 'minimax' in lower:
        return template_tictactoe()
    if 'sudoku' in lower:
        return template_sudoku()
    if 'knapsack' in lower or 'genetic' in lower or 'tsp' in lower:
        return template_genetic()
    if 'perceptron' in lower:
        return template_perceptron()
    if 'fuzzy' in lower:
        return template_fuzzy()
    if 'database' in lower or 'student' in lower or 'vehicle' in lower or 'city' in lower or 'hospital' in lower or 'admission' in lower or 'course' in lower or 'weather' in lower or 'family' in lower or 'medical' in lower or 'knowledge' in lower or 'inference' in lower or 'animal' in lower or 'employee' in lower or 'automobile' in lower or 'university' in lower:
        return template_generic_prolog_launcher(folder_name)
    if 'dfs' in lower or 'bfs' in lower:
        return template_bfs() if 'bfs' in lower else template_dfs()
    if 'search' in lower:
        return template_best_first()
    return template_generic(folder_name)


def main():
    for folder in sorted(root.glob('Experiment_*')):
        code_file = folder / 'source_code.py'
        if not code_file.exists():
            continue
        content = get_content(folder.name)
        code_file.write_text(content, encoding='utf-8')
        print(f'Updated: {code_file}')


if __name__ == '__main__':
    main()
