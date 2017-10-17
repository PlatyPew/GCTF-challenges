#!/usr/bin/env python2

PRINT_FUNCTION = 'n(){ /*/??n/???n?f ${@}; }; f(){ n ${#}; };'
START_PRINT = '$(n $('
END_PRINT = '))'
START_CHAR = 'n \\\\\\\\`'
END_CHAR = '`;'
cmd = list(raw_input('Enter command here > '))
arguments = [PRINT_FUNCTION+START_PRINT]
for i in cmd:
	letter = [START_CHAR]
	octal = list(oct(ord(i))[1:])
	for num in octal:
		num = int(num)
		letter.append('f ' + '\"\" ' * num + '; ')
	letter.append(END_CHAR)
	arguments.append(''.join(letter))
arguments.append(END_PRINT)
print ''.join(arguments)
