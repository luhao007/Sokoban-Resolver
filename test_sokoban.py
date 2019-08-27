import unittest

from sokoban import CannotMoveError, SokobanCore


class SokobanCoreTestCase(unittest.TestCase):

    def setUp(self):
        self.sokoban_map = [[0, 0, 0, 8, 8, 8, 0, 0, 0],
                            [0, 0, 0, 8, 1, 8, 0, 0, 0],
                            [0, 0, 0, 8, 2, 8, 0, 0, 0],
                            [8, 8, 8, 8, 0, 8, 8, 8, 8],
                            [8, 1, 2, 0, 4, 0, 2, 1, 8],
                            [8, 8, 8, 8, 0, 8, 8, 8, 8],
                            [0, 0, 0, 8, 2, 8, 0, 0, 0],
                            [0, 0, 0, 8, 1, 8, 0, 0, 0],
                            [0, 0, 0, 8, 8, 8, 0, 0, 0]]
        self.sokoban = SokobanCore(self.sokoban_map)

    def test_current_map(self):
        m = self.sokoban.get_current_map()
        self.assertEqual(m, self.sokoban_map)

        self.sokoban.up()
        expected = [[0, 0, 0, 8, 8, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [8, 8, 8, 8, 4, 8, 8, 8, 8],
                    [8, 1, 2, 0, 0, 0, 2, 1, 8],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 8, 8, 0, 0, 0]]
        m = self.sokoban.get_current_map()
        self.assertEqual(m, expected)

    def test_pos(self):
        self.assertEqual(self.sokoban.pos, (4, 4))
        self.sokoban.up()
        self.assertEqual(self.sokoban.pos, (4, 3))

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
        expected = [[0, 0, 0, 8, 8, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [8, 8, 8, 8, 4, 8, 8, 8, 8],
                    [8, 1, 2, 0, 0, 0, 2, 1, 8],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 8, 8, 0, 0, 0]]
        m = self.sokoban.get_current_map()
        self.assertEqual(m, expected)

        self.sokoban.up()
        expected = [[0, 0, 0, 8, 8, 8, 0, 0, 0],
                    [0, 0, 0, 8, 3, 8, 0, 0, 0],
                    [0, 0, 0, 8, 4, 8, 0, 0, 0],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [8, 1, 2, 0, 0, 0, 2, 1, 8],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 8, 8, 0, 0, 0]]
        m = self.sokoban.get_current_map()
        self.assertEqual(m, expected)

        with self.assertRaises(CannotMoveError):
            self.sokoban.up()

    def test_move_down(self):
        self.sokoban.down()
        expected = [[0, 0, 0, 8, 8, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [8, 1, 2, 0, 0, 0, 2, 1, 8],
                    [8, 8, 8, 8, 4, 8, 8, 8, 8],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 8, 8, 0, 0, 0]]
        m = self.sokoban.get_current_map()
        self.assertEqual(m, expected)

        self.sokoban.down()
        expected = [[0, 0, 0, 8, 8, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [8, 1, 2, 0, 0, 0, 2, 1, 8],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [0, 0, 0, 8, 4, 8, 0, 0, 0],
                    [0, 0, 0, 8, 3, 8, 0, 0, 0],
                    [0, 0, 0, 8, 8, 8, 0, 0, 0]]
        m = self.sokoban.get_current_map()
        self.assertEqual(m, expected)

        with self.assertRaises(CannotMoveError):
            self.sokoban.down()

    def test_move_left(self):
        self.sokoban.left()
        expected = [[0, 0, 0, 8, 8, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [8, 1, 2, 4, 0, 0, 2, 1, 8],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 8, 8, 0, 0, 0]]
        m = self.sokoban.get_current_map()
        self.assertEqual(m, expected)

        self.sokoban.left()
        expected = [[0, 0, 0, 8, 8, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [8, 3, 4, 0, 0, 0, 2, 1, 8],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 8, 8, 0, 0, 0]]
        m = self.sokoban.get_current_map()
        self.assertEqual(m, expected)

        with self.assertRaises(CannotMoveError):
            self.sokoban.left()

    def test_move_right(self):
        self.sokoban.right()
        expected = [[0, 0, 0, 8, 8, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [8, 1, 2, 0, 0, 4, 2, 1, 8],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 8, 8, 0, 0, 0]]
        m = self.sokoban.get_current_map()
        self.assertEqual(m, expected)

        self.sokoban.right()
        expected = [[0, 0, 0, 8, 8, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [8, 1, 2, 0, 0, 0, 4, 3, 8],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 8, 8, 0, 0, 0]]
        m = self.sokoban.get_current_map()
        self.assertEqual(m, expected)

        with self.assertRaises(CannotMoveError):
            self.sokoban.right()

    def test_move_boxes(self):
        sokoban = SokobanCore([[0, 0, 8, 8, 8, 0, 0],
                               [0, 0, 8, 2, 8, 0, 0],
                               [8, 8, 8, 2, 8, 8, 8],
                               [8, 2, 2, 4, 2, 2, 8],
                               [8, 8, 8, 2, 8, 8, 8],
                               [0, 0, 8, 2, 8, 0, 0],
                               [0, 0, 8, 8, 8, 0, 0]])

        with self.assertRaises(CannotMoveError):
            sokoban.up()
        with self.assertRaises(CannotMoveError):
            sokoban.down()
        with self.assertRaises(CannotMoveError):
            sokoban.left()
        with self.assertRaises(CannotMoveError):
            sokoban.right()

    def test_multiple_levels(self):
        sokoban = SokobanCore([[[0, 4]], [[4, 0]]])
        self.assertEqual(sokoban.get_current_map(), [[0, 4]])
        sokoban.next_level()
        self.assertEqual(sokoban.get_current_map(), [[4, 0]])

        with self.assertRaises(Exception):
            sokoban.next_level()


if __name__ == '__main__':
    unittest.main()
