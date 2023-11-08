# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, check_winner, update_board

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
