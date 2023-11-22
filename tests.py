import unittest
from logic import HumanPlayer, BotPlayer, TicTacToeGame

class TestTicTacToeGame(unittest.TestCase):

    def test_initial_empty_board(self):
        game = TicTacToeGame(HumanPlayer('X'), BotPlayer('O'))
        self.assertEqual(game.board.board, [[None]*3 for _ in range(3)])

    def test_initialization_with_two_human_players(self):
        player1 = HumanPlayer('X')
        player2 = HumanPlayer('O')
        game = TicTacToeGame(player1, player2)
        self.assertIsInstance(game.players[0], HumanPlayer)
        self.assertIsInstance(game.players[1], HumanPlayer)
        self.assertEqual(player1.symbol, 'X')
        self.assertEqual(player2.symbol, 'O')

    def test_initialization_with_human_and_bot_player(self):
        player1 = HumanPlayer('X')
        player2 = BotPlayer('O')
        game = TicTacToeGame(player1, player2)
        self.assertIsInstance(game.players[0], HumanPlayer)
        self.assertIsInstance(game.players[1], BotPlayer)
        self.assertEqual(player1.symbol, 'X')
        self.assertEqual(player2.symbol, 'O')

    def test_alternate_turns(self):
        game = TicTacToeGame(HumanPlayer('X'), HumanPlayer('O'))
        self.assertEqual(game.current_player, 0)
        game.switch_player()
        self.assertEqual(game.current_player, 1)

    def test_winning_conditions(self):
        # Test for a row win
        game = TicTacToeGame(HumanPlayer('X'), HumanPlayer('O'))
        for col in range(3):
            game.board.update_board(0, col, 'X')
        self.assertEqual(game.check_winner(), 'X')

        # Tests for column win, diagonal win, and no winner

    def test_detect_draw(self):
        game = TicTacToeGame(HumanPlayer('X'), HumanPlayer('O'))
        draw_moves = [(0,0,'X'), (0,1,'O'), (0,2,'X'),
                      (1,0,'O'), (1,1,'X'), (1,2,'O'),
                      (2,0,'O'), (2,1,'X'), (2,2,'O')]
        for row, col, player in draw_moves:
            game.board.update_board(row, col, player)
        self.assertIsNone(game.check_winner())

    def test_play_only_in_viable_spots(self):
        game = TicTacToeGame(HumanPlayer('X'), HumanPlayer('O'))
        game.board.update_board(0, 0, 'X')
        self.assertFalse(game.board.is_valid_move(0, 0))

    def test_correct_winner_detection(self):
        game = TicTacToeGame(HumanPlayer('X'), HumanPlayer('O'))
        game.board.board = [['X', 'X', 'X'],
                            [None, 'O', 'O'],
                            ['O', None, None]]
        self.assertEqual(game.check_winner(), 'X')


if __name__ == '__main__':
    unittest.main()
