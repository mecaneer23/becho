#!/bin/env python3

from curses import wrapper, use_default_colors
from sys import argv

def main(stdscr, message):
    y, x = stdscr.getmaxyx()
    use_default_colors()
    stdscr.clear()
    stdscr.addstr(y // 2 - 5, x // 2 - len(message) // 2, message)
    stdscr.refresh()
    return stdscr.getkey()

wrapper(main, " ".join(argv[1:]))
