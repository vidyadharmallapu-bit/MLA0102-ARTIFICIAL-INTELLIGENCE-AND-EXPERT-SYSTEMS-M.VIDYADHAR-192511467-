"""Choose an optimal Tic-Tac-Toe move with minimax and alpha-beta pruning."""

EMPTY = " "
WIN_LINES = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
)


def winner(board):
    for first, second, third in WIN_LINES:
        if board[first] != EMPTY and board[first] == board[second] == board[third]:
            return board[first]
    return None


def minimax(board, player, alpha, beta, depth=0):
    result = winner(board)
    if result == "X":
        return 10 - depth, None
    if result == "O":
        return depth - 10, None
    moves = [index for index, cell in enumerate(board) if cell == EMPTY]
    if not moves:
        return 0, None

    best_move = None
    if player == "X":
        best_score = float("-inf")
        for move in moves:
            board[move] = player
            score, _ = minimax(board, "O", alpha, beta, depth + 1)
            board[move] = EMPTY
            if score > best_score:
                best_score, best_move = score, move
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
    else:
        best_score = float("inf")
        for move in moves:
            board[move] = player
            score, _ = minimax(board, "X", alpha, beta, depth + 1)
            board[move] = EMPTY
            if score < best_score:
                best_score, best_move = score, move
            beta = min(beta, best_score)
            if beta <= alpha:
                break
    return best_score, best_move


def main():
    board = [EMPTY] * 9
    score, move = minimax(board, "X", float("-inf"), float("inf"))
    board[move] = "X"
    print("AI (X) best move on an empty board:", move + 1)
    print("Board after the move:")
    for row in range(0, 9, 3):
        print(" | ".join(cell if cell != EMPTY else str(index + 1)
                         for index, cell in enumerate(board[row:row + 3], start=row)))
        if row < 6:
            print("---------")
    print("Minimax score:", score)


if __name__ == "__main__":
    main()