# Sokoban-Resolver
[![](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/download/)
![Python application](https://github.com/luhao007/Sokoban-Resolver/workflows/Python%20application/badge.svg)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/7ea65c19c8014e4cb4dd991d457d6434)](https://www.codacy.com/gh/luhao007/Sokoban-Resolver/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=luhao007/Sokoban-Resolver&amp;utm_campaign=Badge_Grade)

The classic Sokoban (box pushing) game, with a resolver yet to build.

## Launching the Game

Run `main.py`

## Play the Game

```
W A S D         Move player
Arrow Keys      Move player
U               Undo last move
R               Reset map
N P             Navigate Map
```

## Levels

The levels are stored in [levels](https://github.com/luhao007/Sokoban-Resolver/tree/master/levels) folder.
The level files are simple text files with each character as one tile.

The tiles are defined in ```SokobanTiles``` class in [sokoban.py](https://github.com/luhao007/Sokoban-Resolver/blob/master/sokoban.py).
It also support the common format of sokoban tiles listed in [Sokoban Wiki](http://www.sokobano.de/wiki/index.php?title=Level_format).

The program support `.slc` format for sokoban level collections.
