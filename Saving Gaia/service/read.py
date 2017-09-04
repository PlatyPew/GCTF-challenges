#!/usr/bin/env python2

import sys,os

if os.path.isfile(sys.argv[1]):
	f = open(sys.argv[1],'r')
	final = []
	for phrase in f.readlines():
		final.append(phrase.strip())
	f.close()
	print ', '.join(final)
else:
	print 'File does not exist!'
