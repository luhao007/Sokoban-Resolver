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


class CannotMoveError(Exception):

    def __str__(self):
        return 'Cannot move.'


class Sokoban(object):

    def __init__(self, sokoban_map):
        self.sokoban_map = sokoban_map
        self.reset()

    def _get_pos(self):
        """Get the current player's position.

        Should only need to be called once when game resets."""
        for y, r in enumerate(self.curr):
            for x, t in enumerate(r):
                if t in (SokobanTiles.PLAYER, SokobanTiles.PLAYER_TARGETED):
                    return (x, y)

    def reset(self):
        """Reset the map to the initial status."""
        self.curr = [[int(i) if i.isnumeric() else 0
                      for i in r if i != '\n']
                     for r in self.sokoban_map]
        self.pos = self._get_pos()
        self.finished = False

    def get_current_map(self):
        """Get the current playing map"""
        return [''.join(str(t) for t in r) + '\n' for r in self.curr]

    def show(self):
        """Print out the current playing map"""
        print(self.get_current_map())

    def check_finish(self):
        """Check whether the game is finished."""
        if all(SokobanTiles.BOX not in r for r in self.curr):
            self.finished = True
            print('Congratulations!')

    def _move(self, x, y):
        """Move the player, should not be called by user directly."""
        if self.finished:
            return

        if not (abs(x) < 2 and abs(y) < 2 and abs(x+y) == 1):
            raise RuntimeError('One step at a time please.')

        c_x, c_y = self.pos
        ahead = self.curr[c_y + y][c_x + x]
        if ahead == SokobanTiles.WALL:
            raise CannotMoveError()
        elif ahead.bit_length() < 2:    # Empty
            self.curr[c_y][c_x] -= SokobanTiles.PLAYER
            self.curr[c_y + y][c_x + x] += SokobanTiles.PLAYER
        elif ahead & SokobanTiles.BOX:
            two_ahead = self.curr[c_y + y*2][c_x + x*2]
            if two_ahead.bit_length() > 1:  # Not Empty
                raise CannotMoveError()

            self.curr[c_y + y][c_x + x] -= SokobanTiles.BOX
            self.curr[c_y + y*2][c_x + x*2] += SokobanTiles.BOX

            self.curr[c_y][c_x] -= SokobanTiles.PLAYER
            self.curr[c_y + y][c_x + x] += SokobanTiles.PLAYER

        self.pos = (c_x + x, c_y + y)
        self.check_finish()

    def up(self):
        """Move up."""
        self._move(0, -1)

    def down(self):
        """Move down."""
        self._move(0, 1)

    def left(self):
        """Move left."""
        self._move(-1, 0)

    def right(self):
        """Move right."""
        self._move(1, 0)

    def moves(self, actions):
        """Apply a list of moves."""
        for a in actions:
            if a in ('u', 'up'):
                self.up()
            elif a in ('d', 'down'):
                self.down()
            elif a in ('l', 'left'):
                self.left()
            elif a in ('r', 'right'):
                self.right()
            else:
                raise RuntimeError('Illigal move: {}'.format(a))


def main():
    with open('levels/1.txt', 'r') as f:
        m = f.readlines()

    d = Sokoban(m)

    d.moves('llruudrrlddd')

    d.show()


if __name__ == '__main__':
    main()
