# Crypto Hotdogs
Crack RSA

<i>Creator - @Platy</i>

## Category
Crypto

## Question
>Our team, the Crypto Hotdogs seek for your help. We have encrypted our flag with the public key. However, some idiot told one of my team members that the command 'rm' means 'remake'. Basically, he removed our private key and we have no idea how to retrieve it. Maybe you can help us.

### Hint
Attack the sausages!

## Setup Guide
Do `make all` in generate directory

## Distribution
Zip file
- Crypto Hotdogs.zip `MD5: 7c153234ded94f19ce764c1d18aca339`
	- Encrypted Data
		- flag.bin
	- RSA Public Key
		- public.pem

## Solution
We can start by extracting the values required to decrypt using `openssl rsa -pubin -text -noout -in public.pem`

We get...
```
Public-Key: (1026 bit)
Modulus:
    02:e4:f4:79:09:96:79:f6:4d:6d:74:c0:9c:92:b1:
    2f:da:a9:87:54:15:72:c7:16:c4:46:d6:cb:b8:61:
    d0:58:71:44:c7:8a:f8:69:91:c8:a2:e6:e5:25:ff:
    11:9a:fe:38:6a:8a:6d:af:cb:fa:68:eb:fa:a8:19:
    79:21:8b:55:f0:a7:19:d1:19:3f:f3:2b:91:f7:75:
    3a:b0:51:ff:fa:84:bc:ee:52:5e:a8:7e:2d:f6:d1:
    f6:ee:af:5b:71:3b:46:5e:59:9f:59:9f:b7:6c:d3:
    a7:22:96:2c:8e:93:51:bd:79:14:6e:bd:33:d3:1a:
    72:ce:2c:88:69:50:1d:42:f1
Exponent:
    01:9c:16:3a:24:9f:6b:76:73:d1:1b:5b:04:7a:ee:
    a1:4d:16:49:70:95:ea:3d:9c:38:ce:d7:d2:a0:33:
    10:d2:97:75:11:06:4b:e0:84:6c:67:20:47:29:9d:
    af:3b:cf:1a:2f:16:b6:1b:c4:0c:c2:d4:6c:d3:d5:
    94:12:f0:57:65:7f:ee:6d:7e:b4:de:ce:79:b6:97:
    da:74:08:74:cb:32:df:74:36:db:e6:04:b1:fa:f6:
    24:96:5e:f4:85:13:ad:68:f3:fa:24:62:58:83:52:
    87:d0:1e:f3:58:f8:a4:b8:1d:dc:35:8a:d8:73:81:
    60:2f:50:8b:58:21:56:66:57
```

Converting those values into decimal, we can start to do a wiener attack.

```python
n = 520316275859250741330538874010308470231426334264616801871666493016007086075445797890794759451875380530489987623268879730099107014063159621305525056827219606398364577634729652794493885213899754990788907349947025033432329837589065410107389462971392241914793652931421652693257772782810129645119919244088929239793

e = 289377209264526855820727274450259859457421384721346456230293171491753636443565433235762257810762808373926575624623601418638285551184729674121675920344102705343816437721078772699907379977775639117096341215590337547272320136741176642429957366626686159071767205913806341983621394108788689168359171722820606912087
```

Using the wiener attack, we get the private exponent of the RSA and rebuild the private key

```python
d = 39242924240998887071343792618081289828911742678942932818058940576925353704023
```

Upon reconstructing the private key...
```
-----BEGIN RSA PRIVATE KEY-----
MIICOQIBAAKBgQLk9HkJlnn2TW10wJySsS/aqYdUFXLHFsRG1su4YdBYcUTHivhp
kcii5uUl/xGa/jhqim2vy/po6/qoGXkhi1XwpxnRGT/zK5H3dTqwUf/6hLzuUl6o
fi320fbur1txO0ZeWZ9Zn7ds06ciliyOk1G9eRRuvTPTGnLOLIhpUB1C8QKBgQGc
Fjokn2t2c9EbWwR67qFNFklwleo9nDjO19KgMxDSl3URBkvghGxnIEcpna87zxov
FrYbxAzC1GzT1ZQS8Fdlf+5tfrTeznm2l9p0CHTLMt90NtvmBLH69iSWXvSFE61o
8/okYliDUofQHvNY+KS4Hdw1ithzgWAvUItYIVZmVwIgVsK1P6gf1kain0MzE0i0
Dcz7Ugl7i8BOb9H/PYuK+lcCQQE8X2P0BZHwMO9cVwz1OdaptTfjpeonCms1lLjh
xiCuxCfmu+DIpiMVztgXZs4S7OawXMgDGugbdgxhHraQBa0NAkECV49x/qCDywiB
LZHINLB1+2l+zRK1u252AkTsV199cnyZUygV0F87CjRGw2T3XqbsShCfCvsYv0Dm
KhF6KIbcdQIgVsK1P6gf1kain0MzE0i0Dcz7Ugl7i8BOb9H/PYuK+lcCIFbCtT+o
H9ZGop9DMxNItA3M+1IJe4vATm/R/z2LivpXAkAqLWTm+cRGDxGj5qkca54PObqT
3urBAuAoQ3OkSmywEMfiHZSARMDqnVZERKVFk1LguMtFaGaRRsgYIyix4dzC
-----END RSA PRIVATE KEY-----
```

We can use openssl do decrypt `flag.bin`

`openssl rsautl -decrypt -in flag.bin -inkey private.pem -out flag.txt`

### Flag
`GCTF{w0w_h0770_d06u}`

## Credits
- https://github.com/pablocelayes/rsa-wiener-attack

## Recommended Reads
- https://en.wikipedia.org/wiki/Wiener%27s_attack
- https://sagi.io/2016/04/crypto-classics-wieners-rsa-attack/
