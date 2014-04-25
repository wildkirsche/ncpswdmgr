import curses
import pswdDB

stdscr = curses.initscr() #intiate window

def start(stdscr):
	curses.noecho()
	curses.cbreak()
	stdscr.keypad(True)

	selection = 0 #first menu
	while True:
		stdscr.clear()
		if selection == 1:
			stdscr.addstr(0, 0, "Create a new DB:")
			stdscr.addstr(1, 0, "Load an old DB:", curses.A_REVERSE)
		else:
			stdscr.addstr(0, 0, "Create a new DB:", curses.A_REVERSE)
			stdscr.addstr(1, 0, "Load an old DB:")
		c = stdscr.getch()
		if c == curses.KEY_UP or c == curses.KEY_DOWN:
			selection += 1
			selection %= 2
		elif c == ord('q') or c == curses.KEY_LEFT:
			break  # Exit the while loop
		elif c == curses.KEY_RIGHT or c == curses.KEY_ENTER: #enter next menulevel
			if selection == 0:
				newDB(stdscr)
			else:
				oldDB(stdscr)

	curses.nocbreak()
	stdscr.keypad(False)
	curses.echo()
	curses.endwin()

def newDB(stdscr):
	curses.echo()
	stdscr.keypad(False)
	
	stdscr.clear() #get path to DB
	stdscr.addstr(0, 0, "Enter path to new DB:")
	stdscr.move(1, 0)
	stdscr.refresh()
	path = stdscr.getstr(1,0).decode()
	
	curses.noecho()
	while True: #get mpswd and reassure
		stdscr.clear() #get mpswd
		stdscr.addstr(0, 0, "Enter new master password")
		stdscr.move(1, 0)
		stdscr.refresh
		mpswd = stdscr.getstr(1,0).decode()
		
		stdscr.clear() #get mpswd again
		stdscr.addstr(0, 0, "Repeat new master password")
		stdscr.move(1, 0)
		stdscr.refresh
		rmpswd = stdscr.getstr(1,0).decode()
		
		if mpswd == rmpswd: #create and save DB
			x = pswdDB.pswdDB(mpswd)
			pswdDB.saveDB(path, x)
			break
		else:
			stdscr.clear()
			stdscr.addstr(0, 0, "Didn't match\tHit any key")
			stdscr.refresh()
			stdscr.getch()

def oldDB(stdscr):
	pass
start(stdscr)
