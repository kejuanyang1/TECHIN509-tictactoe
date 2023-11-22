# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

import random

# GameBoard Class
class GameBoard:
    def __init__(self):
        self.board = self.make_empty_board()

    @staticmethod
    def make_empty_board():
        return [[None for _ in range(3)] for _ in range(3)]

    def is_valid_move(self, row, col):
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] is None

    def update_board(self, row, col, player):
        if self.is_valid_move(row, col):
            self.board[row][col] = player
            return True
        return False
    
    def is_draw(self):
        return all(all(cell is not None for cell in row) for row in self.board)
    
    def display(self):
        for row in self.board:
            print([' ' if cell is None else cell for cell in row])

# Player Classes
class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, board):
        raise NotImplementedError

class HumanPlayer(Player):
    def make_move(self, board):
        row, col = map(int, input("Enter row and column separated by space: ").split())
        while not board.update_board(row, col, self.symbol):
            print("Invalid move. Try again.")
            row, col = map(int, input("Enter row and column separated by space: ").split())

class BotPlayer(Player):
    def make_move(self, board):
        row, col = random.randint(0, 2), random.randint(0, 2)
        while not board.update_board(row, col, self.symbol):
            row, col = random.randint(0, 2), random.randint(0, 2)

# TicTacToeGame Class
class TicTacToeGame:
    def __init__(self, player1, player2):
        self.board = GameBoard()
        self.players = [player1, player2]
        self.current_player = 0

    def switch_player(self):
        self.current_player = 1 - self.current_player

    def check_winner(self):
        board = self.board.board
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
                return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
            return board[0][2]
        return None

    def play(self):
        winner = None
        while winner is None:
            self.board.display()
            print("Player", self.players[self.current_player].symbol, "take a turn!")
            self.players[self.current_player].make_move(self.board)
            winner = self.check_winner()
            if winner is None:
                self.switch_player()
        print(winner, "is the winner!")