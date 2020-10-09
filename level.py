import copy
import enum
import itertools
from xml.etree import ElementTree


class SokobanTiles(enum.IntEnum):

    EMPTY = 0
    TARGET = 1
    BOX = 2
    BOX_TARGETED = 3
    PLAYER = 4
    PLAYER_TARGETED = 5
    WALL = 8


SokobanTileMap = {
    ' ': SokobanTiles.EMPTY,
    '.': SokobanTiles.TARGET,
    '$': SokobanTiles.BOX,
    '*': SokobanTiles.BOX_TARGETED,
    '@': SokobanTiles.PLAYER,
    '#': SokobanTiles.WALL,
}


class SokobanLevel(object):

    def __init__(self, level=None):
        self.curr_map = 0

        if isinstance(level, int) or \
           isinstance(level, str) and level.isdigit():
            self.load_text('levels/{}.txt'.format(level))
        elif isinstance(level, str) and level.endswith('txt'):
            self.load_text(level)
        elif isinstance(level, str) and level.endswith('slc'):
            self.load_slc(level)
        elif isinstance(level, list):
            self.load_list(level)
        else:
            raise ValueError('Unknown level: {}'.format(level))

    def get_map(self):
        return copy.deepcopy(self.sokoban_map[self.curr_map])

    def next_level(self):
        if self.curr_map + 1 < len(self.sokoban_map):
            self.curr_map += 1
        else:
            raise ValueError('No more map!')

    def generate_map(self, l):
        valid = [v.value for v in SokobanTiles] + \
                [str(v.value) for v in SokobanTiles] + \
                list(SokobanTileMap.keys()) + \
                ['\n']
        tiles = set(itertools.chain(*l))
        invalid = tiles.difference(valid)
        if invalid:
            raise ValueError('Invalid tiles: {}'.format(invalid))

        return [[int(SokobanTileMap.get(t, t))
                 for t in r if t != '\n']
                for r in l]

    def load_list(self, map_list):
        if isinstance(map_list[0][0], list):
            # multiple levels
            self.sokoban_map = [self.generate_map(l) for l in map_list]
        else:
            # single level
            self.sokoban_map = [self.generate_map(map_list)]

    def load_text(self, file_name):
        with open(file_name, 'r') as f:
            sokoban_map = f.readlines()

        self.sokoban_map = [self.generate_map(sokoban_map)]

    def load_slc(self, file_name):
        tree = ElementTree.parse(file_name)
        root = tree.getroot()
        self.sokoban_map = []
        for l in root.iter('Level'):
            self.sokoban_map.append(self.generate_map([r.text for r in l]))


def main():
    level = SokobanLevel('levels/Original.slc')
    from pprint import pprint
    pprint(level.sokoban_map[0])


if __name__ == '__main__':
    main()
