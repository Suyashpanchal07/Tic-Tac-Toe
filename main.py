import math

# Initialize the board
board = ['' for _ in range(9)]

# Function to print the board
def print_board(board):
    for i in range(3):
        print(board[i*3:(i+1)*3])
    print()

# Function to check for a winner
def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != '':
            return board[combo[0]]
    return None

# Function to check if the board is full
def is_full(board):
    return all(cell != '' for cell in board)

# Minimax function
def minimax(board, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
    winner = check_winner(board)
    if winner == 'X':
        return -10 + depth
    elif winner == 'O':
        return 10 - depth
    elif is_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == '':
                board[i] = 'O'
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ''
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == '':
                board[i] = 'X'
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ''
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# Function to find the best move
def find_best_move(board):
    best_move = None
    best_value = -math.inf
    for i in range(9):
        if board[i] == '':
            board[i] = 'O'
            move_value = minimax(board, 0, False)
            board[i] = ''
            if move_value > best_value:
                best_value = move_value
                best_move = i
    return best_move

# Function to handle the gameplay
def play_game():
    current_player = 'X'  # Human starts as 'X'
    while True:
        print_board(board)
        if current_player == 'X':
            move = int(input("Enter your move (1-9): "))-1
            if board[move] == '':
                board[move] = 'X'
                if check_winner(board) or is_full(board):
                    break
                current_player = 'O'
            else:
                print("Invalid move. Try again.")
        else:
            print("AI is making its move...")
            move = find_best_move(board)
            board[move] = 'O'
            if check_winner(board) or is_full(board):
                break
            current_player = 'X'

    print_board(board)
    winner = check_winner(board)
    if winner:
        print(f"Winner: {winner}")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()

