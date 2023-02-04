import curses
import time

def main(str):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    ZELENA = curses.color_pair(1)
    CERVENA = curses.color_pair(2)
    ORANZOVA = curses.color_pair(3)
    while True:
        str.clear()
        str.addstr("Nejlepší hra na světě, chceš hrát? ")
        str.addstr("(Y)es", ZELENA); str.addstr("/"); str.addstr("(N)o", CERVENA); str.addstr("/"); str.addstr("(Q)uit", ORANZOVA); str.addstr(": ")
        str.refresh()
        ano_nebo_ne = str.getkey().upper()
        if ano_nebo_ne == "Q" or ano_nebo_ne == "N":
            exit()
        elif ano_nebo_ne == "Y":
            str.clear()
            x, y = 10, 10
            while True:
                str.addstr(x, y, "@")
                str.refresh()
                key = str.getkey().upper()
                if key == "A":
                    str.addstr(x, y, "")
                    y -= 1
                    str.addstr(x, y, "@")
                str.refresh()

curses.wrapper(main)