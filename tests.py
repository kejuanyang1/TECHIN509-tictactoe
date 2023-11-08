import unittest
import logic

class TestLogic(unittest.TestCase):

    def test_check_winner(self):        
        boards = [
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

        for board, expected_winner in boards:
            with self.subTest(board=board):
                self.assertEqual(logic.check_winner(board), expected_winner)




if __name__ == '__main__':
    unittest.main()
