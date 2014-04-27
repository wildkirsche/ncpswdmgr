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
	stdscr.keypad(True)

def oldDB(stdscr):
	curses.echo()
	stdscr.keypad(False)
	
	stdscr.clear() #get path to DB
	stdscr.addstr(0, 0, "Enter path to DB:")
	stdscr.move(1, 0)
	stdscr.refresh()
	path = stdscr.getstr(1,0).decode()
	
	DB = pswdDB.loadDB(path)
	
	curses.noecho()
	stdscr.keypad(True)
	
	selection = 0 #first menu
	while True:
		stdscr.clear()
		if selection == 1:
			stdscr.addstr(0, 0, "Save password:")
			stdscr.addstr(1, 0, "Load password:", curses.A_REVERSE)
		else:
			stdscr.addstr(0, 0, "Save password:", curses.A_REVERSE)
			stdscr.addstr(1, 0, "Load password:")
		c = stdscr.getch()
		if c == curses.KEY_UP or c == curses.KEY_DOWN:
			selection += 1
			selection %= 2
		elif c == ord('q') or c == curses.KEY_LEFT:
			break  # Exit the while loop
		elif c == curses.KEY_RIGHT or c == curses.KEY_ENTER: #enter next menulevel
			if selection == 0:
				newDB(stdscr, DB)
			else:
				oldDB(stdscr, DB)

def oldPswd(stdscr, DB):
	curses.echo()
	stdscr.keypad(False)
	
	stdscr.clear()
	stdscr.addstr(0, 0, "Enter site name:")
	stdscr.move(1, 0)
	stdscr.refresh()
	site = stdscr.getstr(1,0).decode()
	
	curses.noecho()
	while True:
		stdscr.clear()
		stdscr.addstr(0, 0, "Enter master password:")
		stdscr.move(1, 0)
		stdscr.refresh()
		mpswd = stdscr.getstr(1,0).decode()
		
		try:
			login, pswd = pswdDB.getpswd(DB, site, mpswd)
			break
		except PasswordError:
			stdscr.clear()
			stdscr.addstr(0, 0, "Didn't match\tHit any key")
			stdscr.getch()
	
	stdscr.clear()
	stdscr.addstr(0, 0, "Login: " + login)
	stdscr.addstr(1, 0, "Password: " + pswd)
	stdscr.addstr(2, 0, "Hit any key")
	stdscr.getch()
	
	curses.echo()
	stdscr.keypad(True)

def newPswd(stdscr, DB):
	curses.echo()
	stdscr.keypad(False)
	
	stdscr.clear()
	stdscr.addstr(0, 0, "Enter site name:")
	stdscr.move(1, 0)
	stdscr.refresh()
	site = stdscr.getstr(1,0).decode()
	
	stdscr.clear()
	stdscr.addstr(0, 0, "Enter login:")
	stdscr.move(1, 0)
	stdscr.refresh()
	login = stdscr.getstr(1,0).decode()
	
	curses.noecho()
	while True: #get mpswd and reassure
		stdscr.clear() #get mpswd
		stdscr.addstr(0, 0, "Enter password")
		stdscr.move(1, 0)
		stdscr.refresh
		pswd = stdscr.getstr(1,0).decode()
		
		stdscr.clear() #get mpswd again
		stdscr.addstr(0, 0, "Repeat password")
		stdscr.move(1, 0)
		stdscr.refresh
		rpswd = stdscr.getstr(1,0).decode()
		
		if pswd == rpswd: #create and save DB
			break
		else:
			stdscr.clear()
			stdscr.addstr(0, 0, "Didn't match\tHit any key")
			stdscr.refresh()
			stdscr.getch()
	
	while True:
		stdscr.clear()
		stdscr.addstr(0, 0, "Enter master password:")
		stdscr.move(1, 0)
		stdscr.refresh()
		mpswd = stdscr.getstr(1,0).decode()
		
		try:
			pswdDB.addpswd(DB, site, login, pswd, mpswd)
			break
		except PasswordError:
			stdscr.clear()
			stdscr.addstr(0, 0, "Didn't match\tHit any key")
			stdscr.getch()
	curses.echo()
	stdscr.keypad(True)

start(stdscr)
