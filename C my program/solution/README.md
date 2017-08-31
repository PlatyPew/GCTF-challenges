This is going to be a long one so hold on to your seats.
The first part is simple. Just press p to print text. The text shown is in base64
```
f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAA8AUAAAAAAABAAAAAAAAAAFAaAAAAAAAAAAAAAEAAOAAJ
AEAAHwAeAAYAAAAFAAAAQAAAAAAAAABAAAAAAAAAAEAAAAAAAAAA+AEAAAAAAAD4AQAAAAAAAAgA
AAAAAAAAAwAAAAQAAAA4AgAAAAAAADgCAAAAAAAAOAIAAAAAAAAcAAAAAAAAABwAAAAAAAAAAQAA
AAAAAAABAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKwKAAAAAAAArAoAAAAAAAAAACAA
AAAAAAEAAAAGAAAA2A0AAAAAAADYDSAAAAAAANgNIAAAAAAAYAIAAAAAAABoAgAAAAAAAAAAIAAA
AAAAAgAAAAYAAADwDQAAAAAAAPANIAAAAAAA8A0gAAAAAADgAQAAAAAAAOABAAAAAAAACAAAAAAA...
```
Decode the base64 and output it to a file. (`echo "base64_here" | base64 -d > filename`)

Using `file <filename>`, the filetype is actually an ELF executable.

Upon running (`chmod +x filename`) the program, the program waits for user input. No matter what input is given, there will always be a `Segmentation fault`.

This is actually just a `printf("Segmentation fault\n");` and does not actually mean a segmentation fault. It's just there to throw people off.
```
0x00000000000007a0 <+128>:	call   0x5d0 <__isoc99_scanf@plt>
0x00000000000007a5 <+133>:	mov    eax,DWORD PTR [rbp-0x44]
0x00000000000007a8 <+136>:	cmp    eax,0xdeadbabe
0x00000000000007ad <+141>:	jne    0x7bb <main+155>
0x00000000000007af <+143>:	mov    eax,0x0
0x00000000000007b4 <+148>:	call   0x810 <winner>
```
We want `eax` to be 0xdeadbabe so it calls the `winner` function.

Convert `0xdeadbabe` to decimal `3735927486`

Entering that as input for the c program, we get the key: `71m3 f0r lunch`
