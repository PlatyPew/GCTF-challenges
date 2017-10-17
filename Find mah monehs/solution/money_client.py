#!/usr/bin/env python3

import socket,re
import time

PRINT_MAZE = True # Prints out the maze from the server
TIME_TO_WAIT = 0.2 # Time to wait before each round
BUFFER_SIZE = 512 ** 2 # Amount of bytes socket listens

PORT = 17454
ADDRESS = 'localhost'

# Formats input data into a dictionary
def gridFormat(buf):
	grid = {}
	buf = buf[2:-2]
	for i,space in enumerate(buf):
		line = re.sub(r'[^-\+@\$]','',space)
		grid[i] = list(line)
	return grid

# Finds the starting and ending points of the maze
def findStartEnd(grid):
	start = []
	end = []
	for row in grid:
		for x,col in enumerate(grid[row]):
			if col == '@':
				start = [row,x]
			elif col == '$':
				end = [row,x]
			if start != [] and end != []:
				break
	return start,end

# Uses flood fill algorithm to solve
def solveMaze(grid,start,end):
	flood = {}
	for y in grid:
		flood[y] = []
		for x in range(len(grid[y])):
			flood[y].append(-1)
	dim = (len(grid),len(grid[0]))

	flood[start[0]][start[1]] = 0
	iteration = 0
	found = False
	while not found:
		for curY in flood:
			for curX in range(len(flood[y])):
				# Move up
				if flood[curY][curX] == iteration:
					if curY - 1 >= 0 :
						if grid[curY-1][curX] == '+' and flood[curY-1][curX] == -1:
							flood[curY-1][curX] = iteration + 1
						elif grid[curY-1][curX] == '$':
							flood[curY-1][curX] = iteration + 1
							found = True
					# Move down
					if curY + 1 < dim[0]:
						if grid[curY+1][curX] == '+' and flood[curY+1][curX] == -1:
							flood[curY+1][curX] = iteration + 1
						elif grid[curY+1][curX] == '$':
							flood[curY+1][curX] = iteration + 1
							found = True
					# Move left
					if curX - 1 >= 0:
						if grid[curY][curX-1] == '+' and flood[curY][curX-1] == -1:
							flood[curY][curX-1] = iteration + 1
						elif grid[curY][curX-1] == '$':
							flood[curY][curX-1] = iteration + 1
							found = True
					# Move right
					if curX + 1 < dim[1]:
						if grid[curY][curX+1] == '+' and flood[curY][curX+1] == -1:
							flood[curY][curX+1] = iteration + 1
						elif grid[curY][curX+1] == '$':
							flood[curY][curX+1] = iteration + 1
							found = True
		iteration += 1

	curY = end[0]
	curX = end[1]
	complete = False
	directions = []
	done = False
	i = 0
	while not complete:
		i += 1
		if curY - 1 >= 0 and not done:
			if flood[curY-1][curX] == flood[curY][curX] - 1:
				curY -= 1
				directions.append('s')
				done = True
				if flood[curY][curX] == 0:
					complete = True
		if curY + 1 < dim[0] and not done:
			if flood[curY+1][curX] == flood[curY][curX] - 1:
				curY += 1
				directions.append('w')
				done = True
				if flood[curY][curX] == 0:
					complete = True
		if curX - 1 >= 0 and not done:
			if flood[curY][curX-1] == flood[curY][curX] - 1:
				curX -= 1
				directions.append('d')
				done = True
				if flood[curY][curX] == 0:
					complete = True
		if curX + 1 < dim[1] and not done:
			if flood[curY][curX+1] == flood[curY][curX] - 1:
				curX += 1
				directions.append('a')
				done = True
				if flood[curY][curX] == 0:
					complete = True

		done = False
	answer = ''.join(directions[::-1])
	return answer

def main():
	try:
		clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		clientsocket.connect((ADDRESS,PORT))
		buf = clientsocket.recv(4096).decode()
		print(buf,end='')
		clientsocket.sendall('\n'.encode())
		start_time = time.time()
		while True:
			buf = clientsocket.recv(BUFFER_SIZE).decode()
			if 'flag' in buf:
				print(buf)
				break
			if PRINT_MAZE:
				print(buf)
			grid = gridFormat(buf.split('\n'))
			start, end = findStartEnd(grid)
			answer = solveMaze(grid,start,end)
			print(answer)
			clientsocket.sendall(answer.encode())
			print()
			time.sleep(TIME_TO_WAIT)
		print("Time taken: {} seconds".format(time.time()-start_time))
		clientsocket.close()
	except socket.error:
		print('Cannot connect')
	except Exception as e:
		print(e)

if __name__ == '__main__':
	main()