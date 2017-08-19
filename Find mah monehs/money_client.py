#!/usr/bin/env python3

import socket,re

def gridFormat(buf):
	grid = {}
	buf = buf[2:-2]
	for i,space in enumerate(buf):
		line = re.sub(r'[^-\+@\$]','',space)
		grid[i] = list(line)
	return grid

def findStartEnd(grid):
	start = []
	end = []
	for row in grid:
		for x,col in enumerate(grid[row]):
			if col == '@':
				start = [row,x]
			elif col == '$':
				end = [row,x]
	return start,end

def solveMaze(grid,start,end):
	'''
	wasHere = {}
	correctPath = {}
	for y in grid:
		wasHere[y] = []
		correctPath[y] = []
		for x in range(len(grid[y])):
			wasHere[y].append(False)
			correctPath[y].append(False)
	dimensions = (len(grid),len(grid[0]))
	'''
	

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost',13337))

buf = clientsocket.recv(4096).decode()
print(buf,end='')
clientsocket.sendall('\n'.encode())


buf = clientsocket.recv(1024**2).decode().split('\n')
grid = gridFormat(buf)
start, end = findStartEnd(grid)
solveMaze(grid,start,end)
	
clientsocket.close()