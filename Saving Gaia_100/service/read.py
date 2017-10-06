#!/usr/bin/env python2

import sys,os

readFile = sys.argv[1]

if 'php' in readFile or 'html' in readFile:
	print 'You do not have permission to read this file!'
elif os.path.isfile(readFile):
	f = open(readFile,'r')
	final = []
	for phrase in f.readlines():
		final.append(phrase.strip())
	f.close()
	print ', '.join(final)
else:
	print 'File does not exist!'
