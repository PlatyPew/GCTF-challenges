#!/usr/bin/env python

ADDRESS = 'localhost'
PORT = 17452

TIME_TO_WAIT = 0.05

import socket, hashlib, random, time

def generate():
	string = ''
	for i in range(random.randint(20,50)):
		string += chr(random.randint(97,122))
	return string

try:
	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientsocket.connect((ADDRESS,PORT))
	buf = clientsocket.recv(4096).decode()
	print(buf)
	clientsocket.sendall('\n'.encode())
	
	for i in range(20):
		buf = clientsocket.recv(128).decode()
		print(buf,end='')
		
		while True:
			value = generate()
			if '\n' in value:
				pass
			elif hashlib.sha512(value.encode('utf-8')).hexdigest()[:2] == '00':
				break
		print(value)
		clientsocket.sendall(value.encode())
		time.sleep(TIME_TO_WAIT)
	print(clientsocket.recv(128).decode())


except socket.error as e:
	print('Cannot connect')
except Exception as e:
	print(e)