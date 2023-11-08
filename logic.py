# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

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
