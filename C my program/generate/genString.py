#!/usr/bin/env python

import sys

if len(sys.argv) != 2:
	print 'Usage: {} string'.format(sys.argv[0])
	sys.exit(0)

final = ''
char = ''
for letter in sys.argv[1]:
	final += str(ord(letter)) + ','
	char += '%c'

print r'printf("Flag: {}\n",{});'.format(char,final[:-1])
