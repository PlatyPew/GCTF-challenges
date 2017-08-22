#!/usr/bin/env python3
# Author: Daryl Lim

from random import choice,randint
import socket
import threading

PORT = 13337 # Change to desired port
TIMEOUT = 1.0

FLAG = 'flag{this_is_a_flag}'

DEFAULT_SIZE = 100 # Must be > 2. More than 10 for best results
ROUNDS = 1 # Number of rounds
STEP = 1
# Colours
BLUE = '\033[94m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
RED = '\033[91m'
END = '\033[0m'
POS = '\033[43m'

maze = {}

# Generate grid length x height
def grid(length=DEFAULT_SIZE,height=DEFAULT_SIZE):
	for row in range(length):
		maze[row] = []
		for col in range(height):
			maze[row].append('-')
	return maze

# Create random paths with starting and ending points
def turtle(maze,path,length=DEFAULT_SIZE,height=DEFAULT_SIZE):
	orig_x = randint(0,length-1)
	orig_y = randint(0,height-1)
	pos_x = orig_x
	pos_y = orig_y
	for step in range(path):
		direction = choice(['up','down','left','right'])
		if (direction is 'up') and (pos_y - STEP >= 0):
			for i in range(STEP):
				pos_y -= 1
				maze[pos_y][pos_x] = '+'
		elif (direction is 'down') and (pos_y + STEP < height):
			for i in range(STEP):
				pos_y += 1
				maze[pos_y][pos_x] = '+'
		elif (direction is 'left') and (pos_x - STEP >= 0):
			for i in range(STEP):
				pos_x -= 1
				maze[pos_y][pos_x] = '+'
		elif (direction is 'right') and (pos_x + STEP < length):
			for i in range(STEP):
				pos_x += 1
				maze[pos_y][pos_x] = '+'

	if orig_x == pos_x and orig_y == pos_y:
		return False, None, None, None
	else:
		maze[orig_y][orig_x] = '@'
		maze[pos_y][pos_x] = '$'
		return True, maze , [orig_x,orig_y], [pos_x,pos_y]

# Formats dictionary for print statement
def display(maze):
	grid = ''
	for row in maze:
		for col in maze[row]:
			if col is '+':
				grid += ' {2}+{0} '
			elif col is '-':
				grid += ' {1}-{0} '
			elif col is '@':
				grid += ' {3}@{0} '
			elif col is '$':
				grid += ' {4}${0} '
			else:
				grid += ' {}{}{} '.format(POS,col,END)
		grid += '\n'
	return grid.format(END,RED,GREEN,YELLOW,BLUE)

# Simulates turtle movement from user input
def check(answer,start,end,maze,length=DEFAULT_SIZE,height=DEFAULT_SIZE):
	orig_x = start[0]
	orig_y = start[1]
	pos_x = orig_x
	pos_y = orig_y

	for direction in answer.strip():
		if direction is 'w':
			if not pos_y - 1 >= 0:
				return False,'U WENT OUT OV TEH GRID!\n'
			elif maze[pos_y-1][pos_x] == '-':
				return False,'U R NOT ALLOWD 2 STEP THAR!\n'
			else:
				pos_y -= 1
		elif direction is 's':
			if not pos_y + 1 < height:
				return False, 'U WENT OUT OV TEH GRID!\n'
			elif maze[pos_y+1][pos_x] == '-':
				return False,'U R NOT ALLOWD 2 STEP THAR!\n'
			else:
				pos_y += 1
		elif direction is 'a':
			if not pos_x - 1 >= 0:
				return False, 'U WENT OUT OV TEH GRID!\n'
			elif maze[pos_y][pos_x-1] == '-':
				return False,'U R NOT ALLOWD 2 STEP THAR!\n'
			else:
				pos_x -= 1
		elif direction is 'd':
			if not pos_x + 1 < length:
				return False, 'U WENT OUT OV TEH GRID!\n'
			elif maze[pos_y][pos_x+1] == '-':
				return False,'U R NOT ALLOWD 2 STEP THAR!\n'
			else:
				pos_x += 1
		else:
			return False, 'INVALID INPUT!\n'
	if pos_x == end[0] and pos_y == end[1]:
		return True, ''
	else:
		maze[pos_y][pos_x] = 'x'
		return False, 'U ENDD IN DA WRONG PLACE!\n\n' + display(maze)

def userInput(connection,tm=TIMEOUT):
	try:
		connection.settimeout(tm)
		answer = connection.recv(4096).decode()
		return answer
	except:
		return False

def gameStart(whut,	connection):
	clientData = '''HALP ME EARN MONEY!

RULEZ:
U HAS %d SECONDZ 2 FIND TEH PATH 2 TEH MONEY!
DO DIS %d TIEMS IN ROW AN U WIN!

TEH {3}@{0} IZ TEH STARTIN POINT
TEH {4}${0} IZ TEH ENDIN POINT
TEH {2}+{0}'S R TEH PATHS DAT U CAN TAEK
TEH {1}-{0}'S R PATHS DAT U CANT TAEK

2 SPECIFY UP U TYPE 'W'
2 SPECIFY LEFT U TYPE 'A'
2 SPECIFY DOWN U TYPE 'S'
2 SPECIFY RITE U TYPE 'D'

For example:
 {1}-{0}  {1}-{0}  {1}-{0}  {1}-{0}  {1}-{0}  {1}-{0}  {1}-{0}  {1}-{0}  {1}-{0}  {1}-{0} 
 {1}-{0}  {1}-{0}  {1}-{0}  {1}-{0}  {1}-{0}  {1}-{0}  {1}-{0}  {1}-{0}  {1}-{0}  {1}-{0} 
 {4}${0}  {2}+{0}  {1}-{0}  {1}-{0}  {1}-{0}  {1}-{0}  {1}-{0}  {1}-{0}  {1}-{0}  {1}-{0} 
 {1}-{0}  {2}+{0}  {2}+{0}  {2}+{0}  {1}-{0}  {2}+{0}  {2}+{0}  {2}+{0}  {1}-{0}  {1}-{0} 
 {1}-{0}  {2}+{0}  {2}+{0}  {1}-{0}  {2}+{0}  {2}+{0}  {2}+{0}  {2}+{0}  {1}-{0}  {1}-{0} 
 {1}-{0}  {2}+{0}  {2}+{0}  {2}+{0}  {2}+{0}  {3}@{0}  {2}+{0}  {2}+{0}  {2}+{0}  {1}-{0} 
 {2}+{0}  {2}+{0}  {2}+{0}  {2}+{0}  {2}+{0}  {2}+{0}  {2}+{0}  {1}-{0}  {1}-{0}  {1}-{0} 
 {2}+{0}  {2}+{0}  {2}+{0}  {2}+{0}  {2}+{0}  {2}+{0}  {1}-{0}  {1}-{0}  {1}-{0}  {1}-{0} 
 {2}+{0}  {2}+{0}  {1}-{0}  {1}-{0}  {2}+{0}  {1}-{0}  {1}-{0}  {1}-{0}  {1}-{0}  {1}-{0} 
 {2}+{0}  {2}+{0}  {1}-{0}  {1}-{0}  {1}-{0}  {1}-{0}  {1}-{0}  {1}-{0}  {1}-{0}  {1}-{0}

TEH ANZWR WILL BE: aaaawwwa

PRES ENTR 2 START!
'''.format(END,RED,GREEN,YELLOW,BLUE) % (int(TIMEOUT),ROUNDS)
	connection.sendall(clientData.encode())
	userInput(connection,tm=60.0)
	
	for i in range(ROUNDS):
		steps = int(DEFAULT_SIZE**2//STEP)
		same = False
		maze = None
		start = None
		end = None
		allow = False

		# Ensure start and end not the same position
		while not same:
			same, maze, start, end = turtle(grid(),steps)

		clientData = '\nROUND {}\n'.format(i+1)
		clientData += display(maze)+'\n'
		clientData += 'PATH 2 TAEK > '
		connection.sendall(clientData.encode())

		answer = userInput(connection)
		if not answer:
			connection.sendall("\nU RAN OUT OV TIEM!\n".encode())
			break

		allow, text = check(answer,start,end,maze)
		
		clientData = (text)
		
		if not allow:
			connection.sendall(clientData.encode())
			break
		else:
			clientData += 'U GOT ${}'.format(i+1)
			connection.sendall(clientData.encode())

	if allow:
		clientData = '\nHER IZ TEH FLAG!\n'
		clientData += FLAG+'\n'
		connection.sendall(clientData.encode())


def main():
	serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		serversocket.bind(('0.0.0.0',PORT))
		serversocket.listen(5)
		print('Socket listening on port',PORT)
		while True:
			connection, address = serversocket.accept()
			t = threading.Thread(target=gameStart, args=(None,connection))
			t.start()
	except KeyboardInterrupt:
		print('\nServer shutting down!')
	except socket.error:
		print('Socket encountered some error!')
	except Exception as e:
		print('Runtime error:\n'+e)
	finally:
		serversocket.close()

if __name__ == '__main__':
	main()
