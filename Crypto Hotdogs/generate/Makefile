all:
	python generate.py
	openssl rsa -in private.pem -pubout -out public.pem
	openssl rsautl -encrypt -in flag.txt -pubin -inkey public.pem -out flag.bin
	rm private.pem
