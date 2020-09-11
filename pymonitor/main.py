import curses
import time
from pymonitor import metrics


def progressbar(scr:curses.initscr()):
    scr.addstr(4,0,"[     ]")
    scr.refresh()
    for i in range(5):
        scr.addstr(4,i+1,"#")
        scr.refresh()
        time.sleep(1)


def main():
    scr = curses.initscr()

    while True:
        scr.addstr(0, 0, "{}".format(metrics.report_memory()))
        scr.refresh()
        progressbar(scr)


if __name__ == "__main__":
    main()
