import base65536

f = open('output.bin','r')
value = ''.join(f.readlines())
f.close()
print(base65536.decode(value).decode())