from level import SokobanLevel, SokobanTiles


class CannotMoveError(Exception):

    def __str__(self):
        return 'Cannot move.'


class SokobanCore(object):

    def __init__(self, level):
        self.level = SokobanLevel(level)
        self.reset()

    @property
    def finished(self):
        return self._finished

    def reset(self):
        """Reset the map to the initial status."""
        self.curr = self.level.get_map()
        self.pos = self.level.get_pos()
        self._finished = False

    def next_level(self):
        self.level.next_level()
        self.reset()

    def get_current_map(self):
        return self.curr

    def check_finish(self):
        """Check whether the game is finished."""
        if all(SokobanTiles.BOX not in r for r in self.curr):
            self._finished = True

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

    d = SokobanCore(m)

    d.moves('llruudrrlddd')

    print(d.get_current_map())


if __name__ == '__main__':
    main()
