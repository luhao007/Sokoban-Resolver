import unittest

from sokoban import SokobanCore, CannotMoveError


class SokobanCoreTestCase(unittest.TestCase):

    def setUp(self):
        self.sokoban_map = ['000888000',
                            '000818000',
                            '000828000',
                            '888808888',
                            '812040218',
                            '888808888',
                            '000828000',
                            '000818000',
                            '000888000']
        self.sokoban = SokobanCore(self.sokoban_map)

    def test_current_map(self):
        m = self.sokoban.get_current_map()
        self.assertEqual(m, self.sokoban_map)

        self.sokoban.up()
        expected = ['000888000',
                    '000818000',
                    '000828000',
                    '888848888',
                    '812000218',
                    '888808888',
                    '000828000',
                    '000818000',
                    '000888000']
        m = self.sokoban.get_current_map()
        self.assertEqual(m, expected)

    def test_get_pos(self):
        self.assertEqual(self.sokoban._get_pos(), (4, 4))
        self.sokoban.up()
        self.assertEqual(self.sokoban._get_pos(), (4, 3))

    def test_reset(self):
        self.sokoban.up()
        self.sokoban.reset()
        m = self.sokoban.get_current_map()
        self.assertEqual(m, self.sokoban_map)

    def test_finish(self):
        self.sokoban.moves('uuddllrrdduurr')
        self.assertTrue(self.sokoban.finished)

    def test_move_up(self):
        self.sokoban.up()
        expected = ['000888000',
                    '000818000',
                    '000828000',
                    '888848888',
                    '812000218',
                    '888808888',
                    '000828000',
                    '000818000',
                    '000888000']
        m = self.sokoban.get_current_map()
        self.assertEqual(m, expected)

        self.sokoban.up()
        expected = ['000888000',
                    '000838000',
                    '000848000',
                    '888808888',
                    '812000218',
                    '888808888',
                    '000828000',
                    '000818000',
                    '000888000']
        m = self.sokoban.get_current_map()
        self.assertEqual(m, expected)

        with self.assertRaises(CannotMoveError):
            self.sokoban.up()

    def test_move_down(self):
        self.sokoban.down()
        expected = ['000888000',
                    '000818000',
                    '000828000',
                    '888808888',
                    '812000218',
                    '888848888',
                    '000828000',
                    '000818000',
                    '000888000']
        m = self.sokoban.get_current_map()
        self.assertEqual(m, expected)

        self.sokoban.down()
        expected = ['000888000',
                    '000818000',
                    '000828000',
                    '888808888',
                    '812000218',
                    '888808888',
                    '000848000',
                    '000838000',
                    '000888000']
        m = self.sokoban.get_current_map()
        self.assertEqual(m, expected)

        with self.assertRaises(CannotMoveError):
            self.sokoban.down()

    def test_move_left(self):
        self.sokoban.left()
        expected = ['000888000',
                    '000818000',
                    '000828000',
                    '888808888',
                    '812400218',
                    '888808888',
                    '000828000',
                    '000818000',
                    '000888000']
        m = self.sokoban.get_current_map()
        self.assertEqual(m, expected)

        self.sokoban.left()
        expected = ['000888000',
                    '000818000',
                    '000828000',
                    '888808888',
                    '834000218',
                    '888808888',
                    '000828000',
                    '000818000',
                    '000888000']
        m = self.sokoban.get_current_map()
        self.assertEqual(m, expected)

        with self.assertRaises(CannotMoveError):
            self.sokoban.left()

    def test_move_left(self):
        self.sokoban.left()
        expected = ['000888000',
                    '000818000',
                    '000828000',
                    '888808888',
                    '812400218',
                    '888808888',
                    '000828000',
                    '000818000',
                    '000888000']
        m = self.sokoban.get_current_map()
        self.assertEqual(m, expected)

        self.sokoban.left()
        expected = ['000888000',
                    '000818000',
                    '000828000',
                    '888808888',
                    '834000218',
                    '888808888',
                    '000828000',
                    '000818000',
                    '000888000']
        m = self.sokoban.get_current_map()
        self.assertEqual(m, expected)

        with self.assertRaises(CannotMoveError):
            self.sokoban.left()

    def test_move_right(self):
        self.sokoban.right()
        expected = ['000888000',
                    '000818000',
                    '000828000',
                    '888808888',
                    '812004218',
                    '888808888',
                    '000828000',
                    '000818000',
                    '000888000']
        m = self.sokoban.get_current_map()
        self.assertEqual(m, expected)

        self.sokoban.right()
        expected = ['000888000',
                    '000818000',
                    '000828000',
                    '888808888',
                    '812000438',
                    '888808888',
                    '000828000',
                    '000818000',
                    '000888000']
        m = self.sokoban.get_current_map()
        self.assertEqual(m, expected)

        with self.assertRaises(CannotMoveError):
            self.sokoban.right()

    def test_move_boxes(self):
        sokoban = SokobanCore(['0088800',
                               '0082800',
                               '8882888',
                               '8224228',
                               '8882888',
                               '0082800',
                               '0088800'])

        with self.assertRaises(CannotMoveError):
            sokoban.up()
        with self.assertRaises(CannotMoveError):
            sokoban.down()
        with self.assertRaises(CannotMoveError):
            sokoban.left()
        with self.assertRaises(CannotMoveError):
            sokoban.right()


if __name__ == '__main__':
    unittest.main()
