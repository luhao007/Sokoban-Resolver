import copy
import enum
import itertools
import os
from xml.etree import ElementTree
import re


class SokobanTiles(enum.IntEnum):

    EMPTY = 0
    TARGET = 1
    BOX = 2
    BOX_WITH_TARGET = 3
    PLAYER = 4
    PLAYER_WITH_TARGET = 5
    WALL = 8


SLCTileMap = {
    ' ': SokobanTiles.EMPTY,
    '.': SokobanTiles.TARGET,
    '$': SokobanTiles.BOX,
    '*': SokobanTiles.BOX_WITH_TARGET,
    '@': SokobanTiles.PLAYER,
    '+': SokobanTiles.PLAYER_WITH_TARGET,
    '#': SokobanTiles.WALL,
}


class SokobanLevel(object):

    def __init__(self, level=None):
        self.load_level(level)

    def load_level(self, level):
        if isinstance(level, int):
            level = f'levels/{level}.txt'

        if isinstance(level, str) and level.endswith('txt'):
            self.load_text(level)
        elif isinstance(level, str) and level.endswith('slc'):
            self.load_slc(level)
        elif isinstance(level, list):
            self.load_list(level)
        else:
            raise ValueError('Unknown level: {}'.format(level))

        self.level = level
        self.curr_map = 0

    def get_map(self):
        return copy.deepcopy(self.maps[self.curr_map])

    def next_level(self):
        if isinstance(self.level, str):
            if self.level.endswith('slc'):
                if self.curr_map + 1 < len(self.maps):
                    self.curr_map += 1
                else:
                    raise ValueError('No more map!')
            else:   # txt
                suffix, i = re.match('(.*?)(\\d+)\\.txt', self.level).groups()
                self.load_level(f'{suffix}{int(i)+1}.txt')
        elif isinstance(self.level, int):
            self.load_level(int(self.level) + 1)

    def prev_level(self):
        if isinstance(self.level, str):
            if self.level.endswith('slc'):
                if self.curr_map:
                    self.curr_map -= 1
                else:
                    raise ValueError('This is the first map!')
            else:   # txt
                suffix, i = re.match('(.*?)(\\d+)\\.txt', self.level).groups()
                self.load_level(f'{suffix}{int(i)-1}.txt')
        elif isinstance(self.level, int):
            self.load_level(int(self.level) - 1)

    def map_info(self):
        if isinstance(self.level, list):
            return 'Custom Map'
        elif isinstance(self.level, int):
            return f'Map: {self.level}.txt'
        else:
            info = 'Map: {}'.format(self.level.split('/')[-1])

            if self.level.endswith('.slc'):
                info += f'\nMaps: {self.curr_map + 1}/{len(self.maps)}'

            return info

    def generate_map(self, l):
        valid = [v.value for v in SokobanTiles] + \
                [str(v.value) for v in SokobanTiles] + \
                list(SLCTileMap.keys()) + \
                ['\n']
        tiles = set(itertools.chain(*l))
        invalid = tiles.difference(valid)
        if invalid:
            raise ValueError('Invalid tiles: {}'.format(invalid))

        return [[int(SLCTileMap.get(t, t))
                 for t in r if t != '\n']
                for r in l]

    def load_list(self, map_list):
        if isinstance(map_list[0][0], list):
            # multiple levels
            self.maps = [self.generate_map(l) for l in map_list]
        else:
            # single level
            self.maps = [self.generate_map(map_list)]

    def load_text(self, file_name):
        with open(file_name, 'r') as f:
            sokoban_map = f.readlines()

        self.maps = [self.generate_map(sokoban_map)]

    def load_slc(self, file_name):
        tree = ElementTree.parse(file_name)
        root = tree.getroot()
        self.maps = []
        for l in root.iter('Level'):
            self.maps.append(self.generate_map([r.text for r in l]))


def main():
    level = SokobanLevel('levels/Original.slc')
    from pprint import pprint
    pprint(level.maps[0])


if __name__ == '__main__':
    main()
