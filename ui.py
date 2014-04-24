import curses

stdscr = curses.initscr() #intiate window

def start(stdscr):
	curses.noecho()
	curses.cbreak()
	stdscr.keypad(True)

	selection = 0 #first menu
	while True:
		if selection == 1:
			stdscr.addstr(0, 0, "Create a new DB:")
			stdscr.addstr(1, 0, "Load an old DB:", curses.A_REVERSE)
		else:
			stdscr.addstr(0, 0, "Create a new DB:", curses.A_REVERSE)
			stdscr.addstr(1, 0, "Load an old  DB:")
		c = stdscr.getch()
		if c == curses.KEY_UP or c == curses.KEY_DOWN:
			selection += 1
			selection %= 2
		elif c == ord('q'):
			break  # Exit the while loop
		elif c == curses.KEY_ENTER: #enter next menulevel
			if selection == 0:
				newDB(stdscr)
			else:
				oldDB(stdscr)

	curses.nocbreak()
	stdscr.keypad(False)
	curses.echo()
	curses.endwin()

def newDB(stdscr):
	pass

def oldDB(stdscr):
	pass
start(stdscr)
