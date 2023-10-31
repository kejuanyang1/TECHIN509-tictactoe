# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board

def is_valid_move(board, row, col):
    """Check if the move is valid."""
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == None

def update_board(board, row, col, player):
    """Update the board with the player's move."""
    if is_valid_move(board, row, col):
        board[row][col] = player
        return True
    return False

def check_winner(board):
    """Check if there's a winner."""
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != None:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != None:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != None:
        return board[0][2]
    return None

if __name__ == '__main__':
    board = make_empty_board()
    current_player = 'X'
    winner = None
    while winner == None:
        print("Player", current_player, "take a turn!")
        # Show the board to the user.
        print('Current Board:')
        for row in board:
            print(row)
        # Input a move from the player.
        row, col = map(int, input("Enter row and column separated by space: ").split())
        # Update board if move is valid 
        while not update_board(board, row, col, current_player):
            print("Invalid move. Try again.")
            row, col = map(int, input("Enter row and column separated by space: ").split())  
        # Check for a winner.
        winner = check_winner(board)
        # Switch players.
        current_player = 'O' if current_player == 'X' else 'X'
    
    print(winner, "is the winner!")
