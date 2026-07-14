import math

# Board visualization positions:
# 0 | 1 | 2
# ---------
# 3 | 4 | 5
# ---------
# 6 | 7 | 8

def print_board(board):
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("-----------")
    print()

def check_winner(board, player):
    # All possible winning combinations
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    return any(all(board[pos] == player for pos in combo) for combo in win_conditions)

def is_board_full(board):
    return " " not in board

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):  # AI is 'O'
        return 1
    if check_winner(board, 'X'):  # Human is 'X'
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = -math.inf
    best_move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def play_game():
    board = [' '] * 9
    print("=========================================")
    print("  TIC-TAC-TOE VS UNBEATABLE AI (Task 2)  ")
    print("=========================================")
    print("Positions are numbered 0 to 8 as follows:")
    print(" 0 | 1 | 2 \n-----------\n 3 | 4 | 5 \n-----------\n 6 | 7 | 8\n")
    
    print_board(board)
    
    while True:
        # Human's Turn
        try:
            move = int(input("Enter your move (0-8): "))
            if move < 0 or move > 8 or board[move] != ' ':
                print("Invalid move! Try again.")
                continue
        except ValueError:
            print("Please enter a valid integer between 0 and 8.")
            continue
            
        board[move] = 'X'
        print_board(board)
        
        if check_winner(board, 'X'):
            print("Wow, you won! (Should be impossible!)")
            break
        if is_board_full(board):
            print("It's a tie!")
            break
            
        # AI's Turn
        print("AI is calculating...")
        ai_move = find_best_move(board)
        board[ai_move] = 'O'
        print(f"AI chose position {ai_move}:\n")
        print_board(board)
        
        if check_winner(board, 'O'):
            print("The AI wins! Better luck next time.")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()
