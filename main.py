import sys
from tkinter import Tk

from ui import SokobanUI


def show_sokoban(sokoban_map, tile_size=50, box_color='brown',
                 target_color='green'):
    root = Tk()
    root.geometry('800x600')
    frame = SokobanUI(sokoban_map, tile_size, box_color, target_color)
    root.mainloop()


def main():
    level = 1 if len(sys.argv) == 1 else sys.argv[1]
    with open('levels/{}.txt'.format(level), 'r') as f:
        m = f.readlines()

    show_sokoban(m, box_color='brown', target_color='green')


if __name__ == '__main__':
    main()
