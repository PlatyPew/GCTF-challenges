#!/usr/bin/env python3
import re
f=open("Potato's Brain.txt","r")
k=f.readlines()
for i in k:
	for j in i:
		if not re.search(r"[^\<\>\-\+\.\[\]]",j):
			print(j,end="")
print()