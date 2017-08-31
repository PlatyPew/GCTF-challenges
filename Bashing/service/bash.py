#!/usr/bin/env python2

import re
import subprocess
import socket
import random
import threading

PORT = 25000

def nachos():
	return '''  _   _            _               
 | \ | |          | |              
 |  \| | __ _  ___| |__   ___  ___ 
 | . ` |/ _` |/ __| '_ \ / _ \/ __|
 | |\  | (_| | (__| | | | (_) \__ \\
 |_| \_|\__,_|\___|_| |_|\___/|___/
'''

def fish():
	return ''' ______ _     _     _           
|  ____(_)   | |   (_)          
| |__   _ ___| |__  _  ___  ___ 
|  __| | / __| '_ \| |/ _ \/ __|
| |    | \__ \ | | | |  __/\__ \\
|_|    |_|___/_| |_|_|\___||___/
'''

def getFlag(con):
	con.sendall('''Foods available
[n]achos
[f]ishies
> ''')
	value = con.recv(256**2).strip()
	if (re.findall('[0-9a-eg-mo-zA-Z]',value) == []):
		final = ''
		output = ''
		if value == 'n':
			final = nachos()
		elif value == 'f':
			final = fish()
		try:
			output = subprocess.check_output(value,stderr=subprocess.STDOUT,shell=True)
		except subprocess.CalledProcessError as e:
			output = 'sh: 1: {} not found'.format(value)
		con.sendall('{}\nHope you enjoy!\n{}\n'.format(final,output))
	else:
		output('Sorry, but we do not serve these here. Maybe next time!')

def start(whut,con):
	try:
		con.sendall('I am a [p]erson, [h]ungry > ')
		value = con.recv(4096).strip()
		if value == 'p':
			con.sendall('Hai human person!\n')
		elif value == 'h':
			getFlag(con)
		else:
			con.sendall('Bye!\n')
			return
	except:
		con.sendall('See you again soon!\n')
	finally:
		con.close()

def main():
	serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		serversocket.bind(('0.0.0.0',PORT))
		serversocket.listen(5)
		print 'Socket listening on port',PORT
		while True:
			connection, address = serversocket.accept()
			threading.Thread(target=start, args=(None,connection)).start()
	except KeyboardInterrupt:
		print('\nServer shutting down!')
	except socket.error:
		print('Socket encountered some error!')
	#except Exception as e:
		#print('Runtime error:\n'+str(e))
	finally:
		serversocket.close()

if __name__ == '__main__':
	main()
