import unittest
from logic import TicTacToeGame, HumanPlayer

class TestTicTacToeGame(unittest.TestCase):

    def test_check_winner(self):        
        test_cases = [
            ([
                ['X', None, 'O'],
                [None, 'X', None],
                [None, 'O', 'X']
            ], 'X'),
            ([
                ['O', 'O', 'O'],
                [None, 'X', 'X'],
                [None, 'X', None]
            ], 'O'),
            ([
                [None, None, None],
                [None, None, None],
                [None, None, None],
            ], None),
            ([
                ['O', None, None],
                [None, 'X', None],
                [None, None, None],
            ], None),
        ]

        for board_state, expected_winner in test_cases:
            with self.subTest(board_state=board_state):
                game = TicTacToeGame(HumanPlayer('X'), HumanPlayer('O'))
                game.board.board = board_state
                self.assertEqual(game.check_winner(), expected_winner)

if __name__ == '__main__':
    unittest.main()
