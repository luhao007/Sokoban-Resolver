import copy
import enum
import itertools
import os
import re
from xml.dom import minidom
from xml.etree import ElementTree


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


class SokobanMap:

    def __init__(self, sokoban_map, map_id=None):
        self.map = self.generate_map(sokoban_map)
        self.id = map_id

    def generate_map(self, sokoban_map):
        valid = [v.value for v in SokobanTiles] + \
                [str(v.value) for v in SokobanTiles] + \
                list(SLCTileMap.keys()) + \
                ['\n']
        tiles = set(itertools.chain(*sokoban_map))
        invalid = tiles.difference(valid)
        if invalid:
            raise ValueError('Invalid tiles: {}'.format(invalid))

        return [[int(SLCTileMap.get(t, t))
                 for t in r if t != '\n']
                for r in sokoban_map]


class SokobanLevel:

    def __init__(self, level=None):
        self.title = None
        self.description = None
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
            raise ValueError(f'Unknown level: {level}')

        self.level = level
        self.curr_map = 0

    def get_map(self):
        return copy.deepcopy(self.maps[self.curr_map].map)

    def next_level(self):
        if isinstance(self.level, str):
            if self.level.endswith('slc'):
                if self.curr_map + 1 >= len(self.maps):
                    raise ValueError('No more map!')
                self.curr_map += 1
            else:   # txt
                suffix, i = re.match('(.*?)(\\d+)\\.txt', self.level).groups()
                self.load_level(f'{suffix}{int(i)+1}.txt')
        elif isinstance(self.level, int):
            self.load_level(int(self.level) + 1)
        elif isinstance(self.level, list):
            if self.curr_map + 1 >= len(self.maps):
                raise ValueError('No more map!')
            self.curr_map += 1

    def prev_level(self):
        if isinstance(self.level, str):
            if self.level.endswith('slc'):
                if not self.curr_map:
                    raise ValueError('This is the first map!')
                self.curr_map -= 1
            else:   # txt
                suffix, i = re.match('(.*?)(\\d+)\\.txt', self.level).groups()
                self.load_level(f'{suffix}{int(i)-1}.txt')
        elif isinstance(self.level, int):
            self.load_level(int(self.level) - 1)
        elif isinstance(self.level, list):
            if not self.curr_map:
                raise ValueError('This is the first map!')
            self.curr_map -= 1

    def map_info(self):
        if isinstance(self.level, list):
            return 'Custom Map'
        if isinstance(self.level, int):
            return f'Map: {self.level}.txt'

        info = 'Map: {}'.format(self.level.split('/')[-1])

        if self.title:
            info += f'\nTitle: {self.title}'
        if len(self.maps) > 1:
            info += f'\nMaps: {self.curr_map + 1}/{len(self.maps)}'

        return info

    def load_list(self, map_list):
        if isinstance(map_list[0][0], list):
            # multiple levels
            self.maps = [SokobanMap(l, i) for i, l in enumerate(map_list)]
        else:
            # single level
            self.maps = [SokobanMap(map_list)]
        self.title = None
        self.description = None

    def load_text(self, file_name):
        with open(file_name, 'r') as f:
            sokoban_map = f.readlines()

        self.maps = [SokobanMap(sokoban_map)]
        self.title = None
        self.description = None

    def load_slc(self, file_name):
        tree = ElementTree.parse(file_name)
        root = tree.getroot()
        self.title = root.find("Title").text.strip()
        self.description = root.find("Description").text.strip()
        self.maps = []
        for level in root.iter('Level'):
            self.maps.append(SokobanMap([r.text for r in level], level.get('Id')))


def convert(folder):
    root = ElementTree.Element('SokobanLevels')
    title = ElementTree.SubElement(root, 'Title')
    title.text = folder.split('/')[-1]
    collection = ElementTree.SubElement(root, 'LevelCollection')
    i = 1
    for file in os.listdir(folder):
        if not file.endswith('.txt'):
            continue

        level = ElementTree.SubElement(collection, 'Level', {'id': str(i)})

        with open('/'.join([folder, file]), 'r') as f:
            for r in f.readlines():
                line = ElementTree.SubElement(level, 'L')
                line.text = r[:-1]

        i += 1
        break

    s = ElementTree.tostring(root, encoding='utf-8', xml_declaration=False)
    parsed = minidom.parseString(s)
    xml = parsed.toprettyxml(indent='  ', encoding='utf-8', newl='\n', xml_declaration=False)

    with open(f'{folder}.xml', 'wb') as f:
        f.write(xml)


def main():
    level = SokobanLevel('levels/Sokoban1.slc')
    print(level.maps[0])


if __name__ == '__main__':
    main()
