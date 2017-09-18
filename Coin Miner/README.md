# Coin Miner
Create program to hash stuff

<i>Creator - @Platy</i>

## Category
Programming

## Question
>I'm running low on cash right now. Luckily, I found this virtual currency that uses inputs that when hashed, produce a hexdigest in which the first 2 characters are '00'. I just need 20 of them. Thanks.
>
>Connect via `nc <ip address> 17451`

### Hint
You can use random character generator

## Setup Guide
Do `bash build.sh`

## Distribution
None.

## Solution
Just create a small program which just generates random strings and hashes them
```python
# Generates random string
def generate():
	string = ''
	for i in range(random.randint(20,50)):
		string += chr(random.randint(97,122))
	return string
```

If the hash starts with '00', send it to the server

Working solution `solution.py` in solution directory

### Flag
`GCTF{70d4y_c01n_m1n3r_70m0rr0w_b17c01n}`

## Credits
None.

## Recommended Reads
None.
