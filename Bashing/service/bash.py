#!/usr/bin/env python2

import re
import os
import sys
import random

out = os.fdopen(sys.stdout.fileno(), 'w', 0)

def output(string,end='\n'):
	sys.stdout = out.write(string+end)

def input(string=''):
	output(string,end='')
	value = raw_input()
	return value

def nachos():
	output('''  _   _            _               
 | \ | |          | |              
 |  \| | __ _  ___| |__   ___  ___ 
 | . ` |/ _` |/ __| '_ \ / _ \/ __|
 | |\  | (_| | (__| | | | (_) \__ \\
 |_| \_|\__,_|\___|_| |_|\___/|___/
''')

def fish():
	output(''' ______ _     _     _           
|  ____(_)   | |   (_)          
| |__   _ ___| |__  _  ___  ___ 
|  __| | / __| '_ \| |/ _ \/ __|
| |    | \__ \ | | | |  __/\__ \\
|_|    |_|___/_| |_|_|\___||___/
''')

def getFlag():
	value = input('''Foods available
[n]achos
[f]ishies
> ''')
	if (re.findall('[0-9a-eg-mo-zA-Z]',value) == []):
		if value == 'n':
			nachos()
		elif value == 'f':
			fish()
		output('Hope you enjoy!')
		output(os.popen(value).read())
	else:
		output('Sorry, but we do not serve these here. Maybe next time!')

def main():
	try:
		value = input('I am a [p]erson, [h]ungry > ')
		if value == 'p':
			output('Hai human person!')
		elif value == 'h':
			getFlag()
		else:
			output('Bye!')
			return
	except:
		output('See you again soon!')

if __name__ == '__main__':
	main()
