#!/usr/bin/env python3
# Author: Daryl Lim

from random import choice,randint
import socket
import threading

PORT = 13337 # Change to desired port
TIMEOUT = 3.0

FLAG = 'flag{this_is_a_flag}'

DEFAULT_SIZE = 5 # Must be > 2. More than 10 for best results
ROUNDS = 50 # Number of rounds
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
				return False,'You went out of the grid!\n'
			elif maze[pos_y-1][pos_x] == '-':
				return False,'You are not allowed to step there!\n'
			else:
				pos_y -= 1
		elif direction is 's':
			if not pos_y + 1 < height:
				return False, 'You went out of the grid!\n'
			elif maze[pos_y+1][pos_x] == '-':
				return False,'You are not allowed to step there!\n'
			else:
				pos_y += 1
		elif direction is 'a':
			if not pos_x - 1 >= 0:
				return False, 'You went out of the grid!\n'
			elif maze[pos_y][pos_x-1] == '-':
				return False,'You are not allowed to step there!\n'
			else:
				pos_x -= 1
		elif direction is 'd':
			if not pos_x + 1 < length:
				return False, 'You went out of the grid!\n'
			elif maze[pos_y][pos_x+1] == '-':
				return False,'You are not allowed to step there!\n'
			else:
				pos_x += 1
		else:
			return False, 'Invalid input!\n'
	if pos_x == end[0] and pos_y == end[1]:
		return True, ''
	else:
		maze[pos_y][pos_x] = 'x'
		return False, 'You ended in the wrong place!\n\n' + display(maze)

def userInput(connection,tm=TIMEOUT):
	try:
		connection.settimeout(tm)
		answer = connection.recv(4096).decode()
		return answer
	except:
		return False

def gameStart(whut,	connection):
	clientData = '''Help me earn money!

Rules:
You have %d seconds to find the a path to the money!
Do this %d times in a row and you win!

The {3}@{0} is the starting point
The {4}${0} is the ending point
The {2}+{0}'s are the paths that you can take
The {1}-{0}'s are paths that you cannot take

To specify up you type 'w'
To specify left you type 'a'
To specify down you type 's'
To specify right you type 'd'

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

The answer will be: aaaasssa

Press enter to start!
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

		clientData = '\nRound {}\n'.format(i+1)
		clientData += display(maze)+'\n'
		clientData += 'Path to take > '
		connection.sendall(clientData.encode())

		answer = userInput(connection)
		if not answer:
			connection.sendall("\nYou ran out of time!\n".encode())
			break

		allow, text = check(answer,start,end,maze)
		
		clientData = (text)
		
		if not allow:
			connection.sendall(clientData.encode())
			break
		else:
			clientData += 'You got ${}'.format(i+1)
			connection.sendall(clientData.encode())

	if allow:
		clientData = 'Here is the flag!\n'
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
