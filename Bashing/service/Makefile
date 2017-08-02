docker:
	gcc v13wF1a6.c -o v13wF1a6
local:
	useradd -m bashing_pwn
	useradd bashing
	gcc v13wF1a6.c -o v13wF1a6
	cp bash.py /home/bashing_pwn/.
	cp flag.txt /home/bashing_pwn/.
	cp v13wF1a6 /home/bashing_pwn/.v13wF1a6
	chown bashing_pwn /home/bashing_pwn/bash.py
	chmod 755 /home/bashing_pwn/bash.py
	chown bashing_pwn /home/bashing_pwn/flag.txt
	chmod 400 /home/bashing_pwn/flag.txt
	chown bashing_pwn /home/bashing_pwn/.v13wF1a6
	chmod 4755 /home/bashing_pwn/.v13wF1a6