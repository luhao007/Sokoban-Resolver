import copy
import enum
import itertools


class SokobanTiles(enum.IntEnum):

    EMPTY = 0
    TARGET = 1
    BOX = 2
    BOX_TARGETED = 3
    PLAYER = 4
    PLAYER_TARGETED = 5
    WALL = 8


class SokobanLevel(object):

    def __init__(self, level=None):
        if isinstance(level, int) or \
           isinstance(level, str) and level.isdigit():
            self.load_text('levels/{}.txt'.format(level))
        elif isinstance(level, str) and level.endswith('txt'):
            self.load_text(level)
        elif isinstance(level, list):
            self.generate_map(level)
        else:
            raise ValueError('Unknown level: {}'.format(level))

    def get_pos(self):
        """Get the current player's position.

        Should only need to be called once when game resets."""
        for y, r in enumerate(self.sokoban_map):
            for x, t in enumerate(r):
                if t in (SokobanTiles.PLAYER, SokobanTiles.PLAYER_TARGETED):
                    return (x, y)

    def get_map(self):
        return copy.deepcopy(self.sokoban_map)

    def generate_map(self, l):
        valid = [v.value for v in SokobanTiles] + \
                [str(v.value) for v in SokobanTiles] + [' ', '\n']
        tiles = set(itertools.chain(*l))
        invalid = tiles.difference(valid)
        if invalid:
            raise ValueError('Invalid tiles: {}'.format(invalid))

        self.sokoban_map = [[0 if t == ' ' else int(t)
                             for t in r if t != '\n']
                            for r in l]

    def load_text(self, file_name):
        with open(file_name, 'r') as f:
            sokoban_map = f.readlines()

        self.generate_map(sokoban_map)
