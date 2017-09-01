# C my program
Testing on writing small scripts or dissassembling programs

<i>Creator - @Platy</i>

## Category
Pwn

## Question
My friend just learnt how to program in the C language. However, he said that something is wrong with his program and wants me to see what's going on... He tried sending me the file through whatsapp but it doesn't allow compiled C files. So he sent me this .txt file. I only know how to program in scratch so I have no idea what to do with this.

## Hint
None.

## Setup
Distibute all files in distrib directory

## Solution
Upon opening `program.txt`, we are greeted with a huge chunk of base64 text. As the title and description would suggest, this is a C program encoded using base64 so most online tools will not be able to decode it properly.
```
f0VMRgIBAQAAAAAAAAAAAAIAPgABAAAAAAVAAAAAAABAAAAAAAAAAIgRAAAAAAAAAAAAAEAAOAAJ
AEAAHgAbAAYAAAAFAAAAQAAAAAAAAABAAEAAAAAAAEAAQAAAAAAA+AEAAAAAAAD4AQAAAAAAAAgA
AAAAAAAAAwAAAAQAAAA4AgAAAAAAADgCQAAAAAAAOAJAAAAAAAAcAAAAAAAAABwAAAAAAAAAAQAA
AAAAAAABAAAABQAAAAAAAAAAAAAAAABAAAAAAAAAAEAAAAAAAKQJAAAAAAAApAkAAAAAAAAAACAA
AAAAAAEAAAAGAAAAEA4AAAAAAAAQDmAAAAAAABAOYAAAAAAAQAIAAAAAAABIAgAAAAAAAAAAIAAA
AAAAAgAAAAYAAAAoDgAAAAAAACgOYAAAAAAAKA5gAAAAAADQAQAAAAAAANABAAAAAAAACAAAAAAA...
```
So, opening the file up in linux, we can use `base64 -d` to decode the text

Save the output to a file do `file <filename>`. Turns out it's a 64-bit ELF executable.

Using `file <filename>`, the filetype is actually an ELF executable.

Giving it the required permissions (chmod), we run the program and this pops up...
```
I have chosen a number between 0 to 10000. Can you guess what it is?
>
```

Upon putting in any input, we are greeted with a `Segmentation Fault`. But it doesn't feel quite right... And that's because the letter 'F' is capitalised! It's obvious that the program is just doing a `printf("Segmentation Fault\n");` Using `strings`, we can confirm that this is true.

```
GCTF{This is not an actual flag get rekt lol. I like fidget spinners}
I have chosen a number between 0 to 10000. Can you guess what it is?
Segmatation Fault
Flag: %c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c
```
There is also a fake flag in there.

So from this point on, we can approach it in 2 ways.
1. Dissasembling the program
2. Bruteforcing the inputs

<b>Disassembling</b>

```asm
0x000000000040061d <+48>:    call   0x4004f0 <__isoc99_scanf@plt>
0x0000000000400622 <+53>:    mov    eax,DWORD PTR [rbp-0xc]
0x0000000000400625 <+56>:    cmp    eax,0x2329
0x000000000040062a <+61>:    jne    0x400638 <main+75>
0x000000000040062c <+63>:    mov    eax,0x0
0x0000000000400631 <+68>:    call   0x400644 <winner>
0x0000000000400636 <+73>:    jmp    0x400642 <main+85>
0x0000000000400638 <+75>:    mov    edi,0x40080b
0x000000000040063d <+80>:    call   0x4004b0 <puts@plt>
0x0000000000400642 <+85>:    leave
0x0000000000400643 <+86>:    ret
```
As we can see, at address `0x0000000000400625`, the program compares `0x2329` and `eax` and if it's the same, it jumps to he winner function!
Converting `0x2329` we get `9001`. Input that in and we get the flag!

<b>Brute forcing</b>

Personally, this is my favourite method. Just write a small shell script that brute forces the input from 0 to 10000. Working script in solution directory

### Flag
`GCTF{c_m4n_70_7h3_r35cu3}`

## Distribution
ASCII text
- program.txt

## Credits
None
