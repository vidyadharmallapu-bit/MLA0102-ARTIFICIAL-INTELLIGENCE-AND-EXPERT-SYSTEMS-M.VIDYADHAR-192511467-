"""Tic-Tac-Toe with Minimax

Beginner-friendly version.
This file uses simple Python loops, lists, and dictionaries.
No heavy libraries or advanced tricks are used.
"""



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
