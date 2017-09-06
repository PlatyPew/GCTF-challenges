# Up the Base
Understanding how Base64 actually works and how it can be extended to higher bases using unicode instead of ascii

<i>Creator - @Platy</i>

## Category
Sanity

## Question
>My friend has always found that twitter was not able to fit his grandfather story with the measly 140 characters that they give. He recently learned about Base Encoding. Since twitter accepts unicode characters he decided to increase the base

### Hint
None.

## Setup Guide
Run `make all`

## Distribution
Bin file seemingly filled with Chinese characters
- output.bin

## Solution
In base64, the characters used are the all the lowercase and upper case letters, zero to nine and '+' and '/' with '=' used as padding

This gives us 64 characters to work with (26+26+10+2)

So how can we find a way to encode something in a higher base if ascii only provides 256 characters only?

Unicode. By using all the 'safe' characters in unicode, we can increase the number of characters we have! This gives us 65536 characters to work with! This allows us to compress the text by half, representing 2 ascii characters in one unicode character (Which explains the Chinese text)

Download the base65536 program in your favourite language and run it. (I'm using Python to do it)

```python
import base65536

f = open('output.bin','r')
value = ''.join(f.readlines())
f.close()
print(base65536.decode(value).decode())
```

### Flag
`GCTF{1f_17_l00k5_57up1d_bu7_17_w0rk5_17_41n7_57up1d}'`

## Credits
None.

## Recommended Reads
[Will YouTube Ever Run Out Of Video IDs?](https://www.youtube.com/watch?v=gocwRvLhDf8)

[base65536](https://github.com/qntm/base65536)