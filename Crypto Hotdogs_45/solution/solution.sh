#!/bin/sh

openssl rsa -pubin -text -noout -in public.pem
python3 wiener_attack/RSAwienerHacker.py
python solution.py
openssl rsautl -decrypt -in flag.bin -inkey private.pem -out flag.txt
cat flag.txt
