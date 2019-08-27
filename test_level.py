import unittest

from level import SokobanLevel


class SokobanLevelTestCase(unittest.TestCase):

    def test_basic(self):
        level = SokobanLevel([[8, 4, 0, 8]])
        self.assertEqual(level.get_map(), [[8, 4, 0, 8]])
        self.assertEqual(level.get_pos(), (1, 0))

    def test_invalid_file_type(self):
        with self.assertRaises(ValueError):
            SokobanLevel('foo.bar')

    def test_invalid_tiles(self):
        with self.assertRaises(ValueError):
            SokobanLevel([[9]])

    def test_multiple_levels(self):
        level = SokobanLevel([[[8, 4, 0, 8]], [[8, 0, 4, 8]]])
        self.assertEqual(len(level.sokoban_map), 2)
        self.assertEqual(level.get_map(), [[8, 4, 0, 8]])
        level.next_level()
        self.assertEqual(level.get_map(), [[8, 0, 4, 8]])

        with self.assertRaises(Exception):
            level.next_level()


if __name__ == '__main__':
    unittest.main()
