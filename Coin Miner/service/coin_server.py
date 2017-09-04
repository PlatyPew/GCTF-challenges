#!/usr/bin/env python3

import socket
import threading
import hashlib

PORT = 31337
TIMEOUT = 60.0

FLAG = 'flag{this_is_a_flag}'

BLUE = '\033[94m'
END = '\033[0m'

def userInput(connection,tm=TIMEOUT):
	try:
		connection.settimeout(tm)
		answer = connection.recv(4096).decode()
		return answer
	except:
		return False

def mine(whut, connection):
	clientData = '''Time to mine some coins!
All you have to do is to provide me with 20 different strings that has 4 zeros in the first 2 characters after being hashed with SHA-512.

Example hashed inputs that are accepted:
{0}00{1}728b3e9af413ad74536e95c3500913a4303b4c965b3eee57fbd0612f9c5ebf5507b17a92d021e67e11d200cea605a04474a3ec0797e488b095676bfc59de22
{0}00{1}eee38b00d27c45425dbb1229d765d82f0853f1b8a99a633d6ccae9ebf79cb35cfa04682c2003ea2c586bcc1c539d01a536a2bfcce7d2390be0b26d55b93932
{0}00{1}525b069d396330d062a02808a9bfe841e9d971ba26a6ff31d0af1a313070587be59c9c6dbc4a41d9df3507ae0ebe2fda80ec28941db1b9bca13b13025f8f66

Of course, you cannot use the same input twice!
Press enter to start!'''.format(BLUE,END)
	connection.sendall(clientData.encode())
	value = userInput(connection)
	if value:
		sent = []
		for i in range(20):
			clientData = 'Input {} > '.format(i+1)
			connection.sendall(clientData.encode())
			value = userInput(connection).strip()
			userHash = hashlib.sha512(value.encode('utf-8')).hexdigest()
			if userHash[:2] == '00' and userHash not in sent:
				sent.append(userHash)
			else:
				clientData = 'Input is invalid\n'
				connection.sendall(clientData.encode())
				connection.close()
				return
		connection.sendall('Good job!\nHere is the flag: {}'.format(FLAG).encode())
		connection.close()
	else:
		clientData = 'You have been kicked for being idle for 1 minute\n'
		connection.sendall(clientData.encode())
		connection.close()
		return

def main():
	serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		serversocket.bind(('0.0.0.0',PORT))
		serversocket.listen(5)
		print('Socket listening on port',PORT)
		while True:
			connection, address = serversocket.accept()
			threading.Thread(target=mine, args=(None,connection)).start()
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