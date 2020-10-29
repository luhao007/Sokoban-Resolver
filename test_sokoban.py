import unittest

from sokoban import CannotMoveError, SokobanCore, SokobanState, Moves


class SokobanStateTestCase(unittest.TestCase):

    def setUp(self):
        m = [[0, 0, 0, 8, 8, 8, 0, 0, 0],
             [0, 0, 0, 8, 1, 8, 0, 0, 0],
             [0, 0, 0, 8, 2, 8, 0, 0, 0],
             [8, 8, 8, 8, 0, 8, 8, 8, 8],
             [8, 1, 2, 0, 4, 0, 2, 1, 8],
             [8, 8, 8, 8, 0, 8, 8, 8, 8],
             [0, 0, 0, 8, 2, 8, 0, 0, 0],
             [0, 0, 0, 8, 1, 8, 0, 0, 0],
             [0, 0, 0, 8, 8, 8, 0, 0, 0]]
        self.state = SokobanState(m)

    def test_move_up(self):
        s = self.state.move(Moves.UP)
        expected = [[0, 0, 0, 8, 8, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [8, 8, 8, 8, 4, 8, 8, 8, 8],
                    [8, 1, 2, 0, 0, 0, 2, 1, 8],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 8, 8, 0, 0, 0]]
        self.assertEqual(s.map, expected)

        s = s.move(Moves.UP)
        expected = [[0, 0, 0, 8, 8, 8, 0, 0, 0],
                    [0, 0, 0, 8, 3, 8, 0, 0, 0],
                    [0, 0, 0, 8, 4, 8, 0, 0, 0],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [8, 1, 2, 0, 0, 0, 2, 1, 8],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 8, 8, 0, 0, 0]]
        self.assertEqual(s.map, expected)

        with self.assertRaises(CannotMoveError):
            s.move(Moves.UP)

    def test_move_down(self):
        s = self.state.move(Moves.DOWN)
        expected = [[0, 0, 0, 8, 8, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [8, 1, 2, 0, 0, 0, 2, 1, 8],
                    [8, 8, 8, 8, 4, 8, 8, 8, 8],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 8, 8, 0, 0, 0]]
        self.assertEqual(s.map, expected)

        s = s.move(Moves.DOWN)
        expected = [[0, 0, 0, 8, 8, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [8, 1, 2, 0, 0, 0, 2, 1, 8],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [0, 0, 0, 8, 4, 8, 0, 0, 0],
                    [0, 0, 0, 8, 3, 8, 0, 0, 0],
                    [0, 0, 0, 8, 8, 8, 0, 0, 0]]
        self.assertEqual(s.map, expected)

        with self.assertRaises(CannotMoveError):
            s.move(Moves.DOWN)

    def test_move_left(self):
        s = self.state.move(Moves.LEFT)
        expected = [[0, 0, 0, 8, 8, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [8, 1, 2, 4, 0, 0, 2, 1, 8],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 8, 8, 0, 0, 0]]
        self.assertEqual(s.map, expected)

        s = s.move(Moves.LEFT)
        expected = [[0, 0, 0, 8, 8, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [8, 3, 4, 0, 0, 0, 2, 1, 8],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 8, 8, 0, 0, 0]]
        self.assertEqual(s.map, expected)

        with self.assertRaises(CannotMoveError):
            s.move(Moves.LEFT)

    def test_move_right(self):
        s = self.state.move(Moves.RIGHT)
        expected = [[0, 0, 0, 8, 8, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [8, 1, 2, 0, 0, 4, 2, 1, 8],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 8, 8, 0, 0, 0]]
        self.assertEqual(s.map, expected)

        s = s.move(Moves.RIGHT)
        expected = [[0, 0, 0, 8, 8, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [8, 1, 2, 0, 0, 0, 4, 3, 8],
                    [8, 8, 8, 8, 0, 8, 8, 8, 8],
                    [0, 0, 0, 8, 2, 8, 0, 0, 0],
                    [0, 0, 0, 8, 1, 8, 0, 0, 0],
                    [0, 0, 0, 8, 8, 8, 0, 0, 0]]
        self.assertEqual(s.map, expected)

        with self.assertRaises(CannotMoveError):
            s.move(Moves.RIGHT)

    def test_move_boxes(self):
        s = SokobanState([[0, 0, 8, 8, 8, 0, 0],
                          [0, 0, 8, 2, 8, 0, 0],
                          [8, 8, 8, 2, 8, 8, 8],
                          [8, 2, 2, 4, 2, 2, 8],
                          [8, 8, 8, 2, 8, 8, 8],
                          [0, 0, 8, 2, 8, 0, 0],
                          [0, 0, 8, 8, 8, 0, 0]])

        with self.assertRaises(CannotMoveError):
            s.move(Moves.UP)
        with self.assertRaises(CannotMoveError):
            s.move(Moves.DOWN)
        with self.assertRaises(CannotMoveError):
            s.move(Moves.LEFT)
        with self.assertRaises(CannotMoveError):
            s.move(Moves.RIGHT)

    def test_pos(self):
        self.assertEqual(self.state.player_pos(), (4, 4))


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
        self.state = SokobanState(self.sokoban_map)
        self.sokoban = SokobanCore(self.sokoban_map)

    def test_basics(self):
        self.assertEqual(self.sokoban.map, self.state.map)
        self.assertEqual(self.sokoban.player_pos,
                         self.state.player_pos())
        self.assertEqual(self.sokoban.finished, self.state.check_finish())

    def test_reset(self):
        self.sokoban.up()
        self.sokoban.reset()
        self.assertEqual(self.sokoban.state, self.state)

    def test_move_many(self):
        self.sokoban.move_many('udlr')
        self.assertEqual(self.sokoban.get_moves(),
                         [Moves.UP, Moves.DOWN, Moves.LEFT, Moves.RIGHT])

    def test_finish(self):
        self.sokoban.move_many('uuddllrrdduurr')
        self.assertTrue(self.sokoban.finished)

    def test_move_up(self):
        self.sokoban.up()
        self.assertEqual(self.sokoban.get_moves(), [Moves.UP])
        self.assertEqual(self.sokoban.state, self.state.move(Moves.UP))

    def test_move_down(self):
        self.sokoban.down()
        self.assertEqual(self.sokoban.get_moves(), [Moves.DOWN])
        self.assertEqual(self.sokoban.state, self.state.move(Moves.DOWN))

    def test_move_left(self):
        self.sokoban.left()
        self.assertEqual(self.sokoban.get_moves(), [Moves.LEFT])
        self.assertEqual(self.sokoban.state, self.state.move(Moves.LEFT))

    def test_move_right(self):
        self.sokoban.right()
        self.assertEqual(self.sokoban.get_moves(), [Moves.RIGHT])
        self.assertEqual(self.sokoban.state, self.state.move(Moves.RIGHT))

    def test_levels(self):
        sokoban = SokobanCore([[[0, 4]], [[4, 0]]])
        self.assertEqual(sokoban.map, [[0, 4]])
        sokoban.next_level()
        self.assertEqual(sokoban.map, [[4, 0]])

        with self.assertRaises(ValueError):
            sokoban.next_level()

        sokoban.prev_level()
        self.assertEqual(sokoban.map, [[0, 4]])

        with self.assertRaises(ValueError):
            sokoban.prev_level()

    def test_undo(self):
        self.sokoban.up()
        self.sokoban.up()
        self.sokoban.undo()
        self.assertEqual(self.sokoban.state, self.state.move(Moves.UP))
        self.assertEqual(self.sokoban.get_moves(), [Moves.UP])


if __name__ == '__main__':
    unittest.main()
