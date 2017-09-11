import socket
import time
import sys

GREEN = '\033[92m'

ADDRESS = 'localhost'
PORT = 9999

def main():
	try:
		clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		clientsocket.connect((ADDRESS,PORT))
		buf = clientsocket.recv(1024).decode()
		clientsocket.sendall('\n'.encode())
		while True:
			buf = clientsocket.recv(1024).decode()
			print(buf,end='')
			if 'GCTF' in buf:
				print()
				break
			elif GREEN in buf:
				clientsocket.sendall('Yes! I will study'.encode())
				print('Yes! I will study')
			else:
				clientsocket.sendall('No! I won\'t study'.encode())
				print('No! I won\'t study')
			time.sleep(0.01)
		clientsocket.close()
	except socket.error:
		print('Cannot connect')
	except Exception as e:
		print(e)

if __name__ == '__main__':
	main()