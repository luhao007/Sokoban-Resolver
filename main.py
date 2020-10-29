import functools
import sys
import textwrap
import tkinter
from tkinter import filedialog, messagebox

from ui import SokobanFrame


class SokobanGame:

    def __init__(self):
        """Classic Sokoban game."""
        self.level = 'levels/1.txt'
        self.tile_size = 50
        self.box_color = 'brown'
        self.target_color = 'green'

        self.root = tkinter.Tk()
        self.root.title('Sokoban')
        self.frame = SokobanFrame(self.root,
                                  self.tile_size,
                                  self.box_color,
                                  self.target_color)

        self.add_menu()

    def set_level(self, level):
        self.frame.set_level(level)

    def open_file(self, *_args):
        level = filedialog.askopenfilename(initialdir='levels/')
        if level:
            self.set_level(level)

    def show_moves(self):
        self.frame.show_moves()

    def add_menu(self):
        menubar = tkinter.Menu(self.root)
        file_menu = tkinter.Menu(menubar, tearoff=False)
        game_menu = tkinter.Menu(menubar, tearoff=False)
        help_menu = tkinter.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="File", underline=0, menu=file_menu)
        menubar.add_cascade(label="Game", underline=0, menu=game_menu)
        menubar.add_cascade(label="Help", underline=0, menu=help_menu)

        file_menu.add_command(label='Open...',
                              command=self.open_file,
                              accelerator='Ctrl+O')
        self.root.bind_all('<Control-o>', self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label='Exit',
                              command=functools.partial(exit, 0),
                              accelerator='Alt+F4')

        game_menu.add_command(label='Show Moves...',
                              command=self.show_moves)

        help_menu.add_command(label='Help...',
                              command=show_help,
                              accelerator='F1')
        self.root.bind_all('<F1>', show_help)

        self.root.config(menu=menubar)

    def show(self):
        if not self.frame.sokoban:
            self.set_level(self.level)

        self.frame.draw()
        self.root.mainloop()


def show_help(*_args):
    msg = """
    W A S D         Move player
    Arrow Keys      Move player
    U               Undo last move
    R               Reset map
    N P             Navigate Maps"""
    msg = textwrap.dedent(msg).strip()
    messagebox.showinfo(title='Help', message=msg)


def main():
    level = 1 if len(sys.argv) == 1 else sys.argv[1]

    s = SokobanGame()
    s.set_level(level)

    s.show()


if __name__ == '__main__':
    main()
