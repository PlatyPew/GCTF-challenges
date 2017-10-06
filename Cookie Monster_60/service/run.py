#!/usr/bin/env python

from subprocess import check_output
from re import sub
import socket
import threading

PORT = 44445
TIMEOUT = 60.0

def userInput(connection,tm=TIMEOUT):
	try:
		connection.settimeout(tm)
		answer = connection.recv(512).decode()
		return answer
	except:
		return False

def exploit(whut,connection):
	connection.sendall('Send nice image please > ')
	exploit = userInput(connection)
	exploit = sub(r'"','',exploit)

	output = check_output(['./phantomjs --cookies-file=cookie.txt image.js \"%s\"' % exploit],shell=True)
	output = sub(r'[\n\t]','',output)
	connection.sendall(output + '\n')
	connection.close()

def main():
	serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		serversocket.bind(('0.0.0.0',PORT))
		serversocket.listen(5)
		print 'Socket listening on port', PORT
		while True:
			connection, address = serversocket.accept()
			threading.Thread(target=exploit, args=(None,connection)).start()
	except KeyboardInterrupt:
		print '\nServer shutting down!'
	except socket.error:
		print 'Socket encountered some error!'
	except Exception as e:
		print 'Runtime error:\n'+str(e)
	finally:
		serversocket.close()


if __name__ == '__main__':
	main()
