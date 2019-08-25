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


if __name__ == '__main__':
    unittest.main()
