import sys
from tkinter import Tk

from ui import SokobanGame


def main():
    level = 1 if len(sys.argv) == 1 else sys.argv[1]

    s = SokobanGame()
    s.set_level(level)

    s.show()


if __name__ == '__main__':
    main()
