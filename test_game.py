import unittest
from main import check_Winner, check_draw


class TestTicTacToe(unittest.TestCase):
    def test_row_win(self):
        board = [
            'X', 'X', 'X',
            '-', '-', 'O',
            '-', '-', 'O',
        ]

        self.assertTrue(check_Winner(board, 'X'))
        self.assertFalse(check_Winner(board, 'O'))


    def test_column_win(self):
        board = [
            'X', 'X', 'O',
            '-', '-', 'O',
            'X', '-', 'O',
        ]

        self.assertTrue(check_Winner(board, 'O'))
        self.assertFalse(check_Winner(board, 'X'))

    def test_diagonal_win(self):
        board = [
            'X', 'X', 'O',
            '-', 'O', 'O',
            'O', '-', 'X',
        ]

        self.assertTrue(check_Winner(board, 'O'))
        self.assertFalse(check_Winner(board, 'X'))


    def test_draw(self):
        board = [
            'X', 'X', 'O',
            'O', 'O', 'X',
            'X', 'O', 'X',
        ]

        self.assertTrue(check_draw(board))

    def test_draw_s(self):
        board = [
            'X', 'X', 'O',
            'O', 'O', 'X',
            '-', 'O', 'X',
        ]

        self.assertFalse(check_draw(board,))



if __name__ == '__main__':
    unittest.main()