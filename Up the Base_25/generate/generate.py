import base65536

hi = '''Base64 is used to encode arbitrary binary data as "plain" text using a small, extremely safe repertoire of 64 (well, 65) characters. Base64 remains highly suited to text systems where the range of characters available is very small -- i.e., anything still constrained to plain ASCII. Base64 encodes 6 bits, or 3/4 of an octet, per character.
However, now that Unicode rules the world, the range of characters which can be considered "safe" in this way is, in many situations, significantly wider. Base65536 applies the same basic principle to a carefully-chosen repertoire of 65,536 (well, 65,792) Unicode code points, encoding 16 bits, or 2 octets, per character. This allows up to 280 octets of binary data to fit in a Tweet.

Link to base65536: https://github.com/qntm/base65536
Anyways thanks for reading, here is the flag: GCTF{1f_17_l00k5_57up1d_bu7_17_w0rk5_17_41n7_57up1d}'''.encode()
f = open('output.bin','w')
f.write(base65536.encode(hi))
f.close()