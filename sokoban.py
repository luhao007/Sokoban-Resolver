import copy
from enum import Enum

from level import SokobanLevel, SokobanTiles


class CannotMoveError(Exception):

    def __str__(self):
        """Return human readable string."""
        return 'Cannot move.'


class Moves(Enum):

    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UP = (0, -1)
    DOWN = (0, 1)


class SokobanState:

    def __init__(self, sokoban_map):
        """State of a Sokoban game."""
        self.map = sokoban_map

    def __eq__(self, other):
        """Check if two maps are the same."""
        return self.map == other.map

    def check_finish(self):
        """Check whether the game is finished."""
        if all(SokobanTiles.BOX not in r for r in self.map):
            return True
        return False

    def player_pos(self):
        """Get the current player's position."""
        for y, r in enumerate(self.map):
            for x, t in enumerate(r):
                if t & SokobanTiles.PLAYER:
                    return (x, y)

        raise RuntimeError('Didnot find player position!')

    def move(self, m: Moves):
        """Move the player, generate a new state."""
        if self.check_finish():
            return self

        x, y = m.value

        m = copy.deepcopy(self.map)
        c_x, c_y = self.player_pos()
        ahead = self.map[c_y + y][c_x + x]

        if ahead == SokobanTiles.WALL:
            raise CannotMoveError()

        if ahead.bit_length() < 2:    # Empty
            m[c_y][c_x] -= SokobanTiles.PLAYER
            m[c_y + y][c_x + x] += SokobanTiles.PLAYER
        elif ahead & SokobanTiles.BOX:
            two_ahead = m[c_y + y*2][c_x + x*2]
            if two_ahead.bit_length() > 1:  # Not Empty
                raise CannotMoveError()

            m[c_y + y][c_x + x] -= SokobanTiles.BOX
            m[c_y + y*2][c_x + x*2] += SokobanTiles.BOX

            m[c_y][c_x] -= SokobanTiles.PLAYER
            m[c_y + y][c_x + x] += SokobanTiles.PLAYER

        new_state = SokobanState(m)
        return new_state


class SokobanCore:

    def __init__(self, level):
        self.level = SokobanLevel(level)
        self.reset()

    def reset(self):
        """Reset the map to the initial status."""
        self.state = SokobanState(self.level.get_map())
        self.moves = []
        self.previous_states = []

    def prev_level(self):
        self.level.prev_level()
        self.reset()

    def next_level(self):
        self.level.next_level()
        self.reset()

    @property
    def map(self):
        return self.state.map

    @property
    def height(self):
        return len(self.map)

    @property
    def width(self):
        return max([len(r) for r in self.map])

    @property
    def player_pos(self):
        return self.state.player_pos()

    @property
    def map_info(self):
        return self.level.map_info()

    def get_moves(self):
        return self.moves

    @property
    def finished(self):
        return self.state.check_finish()

    def move(self, m: Moves):
        new_state = self.state.move(m)
        self.previous_states.append(self.state)
        self.moves.append(m)
        self.state = new_state

    def up(self):
        self.move(Moves.UP)

    def down(self):
        self.move(Moves.DOWN)

    def left(self):
        self.move(Moves.LEFT)

    def right(self):
        self.move(Moves.RIGHT)

    def move_many(self, actions):
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

    def undo(self):
        if not self.previous_states:
            return

        self.state = self.previous_states.pop(-1)
        self.moves.pop(-1)


def main():
    with open('levels/1.txt', 'r') as f:
        m = f.readlines()

    d = SokobanCore(m)

    d.move_many('llruudrrlddd')

    print(d.map)
    print(d.get_moves())


if __name__ == '__main__':
    main()
