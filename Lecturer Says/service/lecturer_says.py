#!/usr/bin/env python3
import socket
import threading
import random
from sys import exit

PORT = 9999
TIMEOUT = 60.0

GREEN = '\033[92m'
RED = '\033[91m'
END = '\033[0m'

FLAG = 'GCTF{p4y_4773n710n_wh3n_l3c7ur3r_15_61v1n6_3x4m_h1n75}'

def userInput(connection,tm=TIMEOUT):
	try:
		connection.settimeout(tm)
		answer = connection.recv(4096).decode()
		return answer
	except:
		connection.sendall('\nToo slow!\n'.encode())
		connection.close()
		exit()

def say(whut,connection):
	connection.sendall('''Welcome to Lecturer Says!
All you have to do is very simple.
When the text is green, you say "Yes! I will study"
If it's red, you say "No! I won't study"

Example:
Lecturer Says: {0}Do your homework{2}
> Yes! I will study

Lecturer Says: {1}Do your homework{2}
> No! I won't study

Press Enter to continue'''.format(GREEN,RED,END).encode())
	userInput(connection,tm=60.0)
	f = open('commands.txt','r')
	commands = f.readlines()
	f.close()
	for i in range(500):
		roundNo = 'Round: {}'.format(i + 1)
		ins = random.choice(commands).strip()
		if random.choice([True,False]):
			connection.sendall('{0}\nLecturer Says: {1}Study for {2}!{3}\n> '.format(roundNo,GREEN,ins,END).encode())
			ans = userInput(connection).strip()
			if ans != 'Yes! I will study':
				connection.sendall('Nope!\n'.encode())
				connection.close()
				exit()
		else:
			connection.sendall('{0}\nLecturer Says: {1}Study for {2}!{3}\n> '.format(roundNo,RED,ins,END).encode())
			ans = userInput(connection).strip()
			if ans != 'No! I won\'t study':
				connection.sendall('Nope!\n'.encode())
				connection.close()
				exit()
	connection.sendall(FLAG.encode())
	connection.close()

def main():
	serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		serversocket.bind(('0.0.0.0',PORT))
		serversocket.listen(5)
		print('Socket listening on port',PORT)
		while True:
			connection, address = serversocket.accept()
			threading.Thread(target=say, args=(None,connection)).start()
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
	