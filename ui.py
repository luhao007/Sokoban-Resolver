import itertools
import math
import sys
import tkinter
from tkinter import messagebox

from PIL import Image, ImageTk

from level import SokobanTiles
from sokoban import CannotMoveError, SokobanCore


class SokobanFrame(tkinter.Frame):

    def __init__(self, tile_size=50, box_color='brown',
                 target_color='green', **kwargs):
        super().__init__()
        self.sokoban = None
        self.tile_size = tile_size

        self.box_color = box_color
        self.target_color = target_color

        image = Image.open('texture/smile.png')
        image = image.resize([int(self.tile_size*0.8)]*2, Image.ANTIALIAS)
        self.player = ImageTk.PhotoImage(image)

        image = Image.open('texture/laugh.png')
        image = image.resize([int(self.tile_size*0.8)]*2, Image.ANTIALIAS)
        self.player_finished = ImageTk.PhotoImage(image)

        self.initUI()

    def set_level(self, level):
        self.sokoban = SokobanCore(level)

        sokoban_map = self.sokoban.get_current_map()
        height = len(sokoban_map) * self.tile_size
        width = max([len(r) for r in sokoban_map]) * self.tile_size

        self.config(width=width, height=height)

        self.draw()

    def draw_box(self, pos):
        x, y = pos
        s = self.tile_size
        self.canvas.create_rectangle(x + s*0.1, y + s*0.1,
                                     x + s*0.9, y + s*0.9,
                                     width=s * 0.1,
                                     outline=self.box_color)

    def draw_player(self, pos):
        x, y = pos
        s = self.tile_size
        image = self.player_finished if self.sokoban.finished else self.player
        self.canvas.create_image(x + s*0.5, y + s*0.5, image=image)

    def draw_target(self, pos):
        x, y = pos
        s = self.tile_size
        self.canvas.create_line(x + s*0.25 + 1, y + s*0.25 + 1,
                                x + s*0.75, y + s*0.75,
                                width=s * 0.1,
                                fill=self.target_color)
        self.canvas.create_line(x + s*0.25 + 1, y + s*0.75 - 1,
                                x + s*0.75, y + s*0.25,
                                width=s * 0.1,
                                fill=self.target_color)

    def draw_wall(self, pos):
        x, y = pos
        s = self.tile_size
        self.canvas.create_rectangle(x, y, x + s, y + s,
                                     outline=self.box_color,
                                     fill=self.box_color)

    def draw(self):
        self.canvas.delete('all')
        if not self.sokoban:
            return

        for r, row in enumerate(self.sokoban.get_current_map()):
            for c, tile in enumerate(row):
                pos = (c*self.tile_size, r*self.tile_size)

                if tile == SokobanTiles.TARGET:
                    self.draw_target(pos)
                elif tile == SokobanTiles.BOX:
                    self.draw_box(pos)
                elif tile == SokobanTiles.BOX_TARGETED:
                    self.draw_box(pos)
                    self.draw_target(pos)
                elif tile & SokobanTiles.PLAYER:
                    self.draw_player(pos)
                elif tile == SokobanTiles.WALL:
                    self.draw_wall(pos)

    def on_key(self, k):
        if self.sokoban.finished:
            return

        mapping = {'Up': 'up',
                   'Down': 'down',
                   'Left': 'left',
                   'Right': 'right',
                   'r': 'reset',
                   'w': 'up',
                   's': 'down',
                   'a': 'left',
                   'd': 'right'}

        action = mapping.get(k.keysym)
        if not action:
            return

        try:
            getattr(self.sokoban, action)()
        except CannotMoveError:
            # TODO: play sound?
            pass

        self.draw()

        if self.sokoban.finished:
            messagebox.showinfo('Congratulations!',
                                'You finished the level, yay!')

    def initUI(self):
        self.bind('<KeyPress>', self.on_key)
        self.pack(fill='both', expand=1)
        self.focus_set()

        self.canvas = tkinter.Canvas(self)
        self.canvas.pack(fill='both', expand=1)


def main():
    root = tkinter.Tk()
    root.geometry('800x600')
    f = SokobanFrame()
    f.set_level(1)
    root.mainloop()

if __name__ == '__main__':
    main()
