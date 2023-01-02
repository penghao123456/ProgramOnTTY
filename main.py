import curses
try:
    stdscr=curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    try:
        curses.start_color()
        canColor=True
    except:
        canColour=False
        pass

    # ---
    stdscr.addstr('%s' % curses.COLORS)
    stdscr.getch()
    # ---

finally:
    if 'stdscr' in locals():
        stdscr.keypad(False)
        curses.echo()
        curses.nocbreak()
        curses.endwin()
