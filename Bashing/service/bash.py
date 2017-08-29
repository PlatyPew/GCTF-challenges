#!/usr/bin/env python2

import re
import os
import random

def nachos():
	print '''  _   _            _               
 | \ | |          | |              
 |  \| | __ _  ___| |__   ___  ___ 
 | . ` |/ _` |/ __| '_ \ / _ \/ __|
 | |\  | (_| | (__| | | | (_) \__ \\
 |_| \_|\__,_|\___|_| |_|\___/|___/
'''

def fish():
	print ''' ______ _     _     _           
|  ____(_)   | |   (_)          
| |__   _ ___| |__  _  ___  ___ 
|  __| | / __| '_ \| |/ _ \/ __|
| |    | \__ \ | | | |  __/\__ \\
|_|    |_|___/_| |_|_|\___||___/
'''

def getFlag():
	input = raw_input('''Foods available
[n]achos
[f]ishies
> ''')
	if (re.findall('[0-9a-eg-mo-zA-Z]',input) == []):
		if input == 'n':
			nachos()
		elif input == 'f':
			fish()
		print 'Hope you enjoy!'
		print os.popen(input).read()
	else:
		print 'Sorry, but we do not serve these here. Maybe next time!'

def main():
	try:
		input = raw_input('I am a [p]erson, [h]ungry > ')
		if input == 'p':
			print 'Hai human person!'
		elif input == 'h':
			getFlag()
		else:
			print 'Bye!'
			return
	except:
		print 'See you again soon!'

if __name__ == '__main__':
	main()
