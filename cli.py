# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import HumanPlayer, BotPlayer, TicTacToeGame

if __name__ == '__main__':
    mode = input("Enter 1 for single player or 2 for two players: ")
    player1 = HumanPlayer('X')
    player2 = BotPlayer('O') if mode == '1' else HumanPlayer('O')
    while 1:
        game = TicTacToeGame(player1, player2)
        game.play()
