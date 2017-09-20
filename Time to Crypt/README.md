# Time to Crypt
Understanding that One-Time-Pad should only be used one time.

<i>Creator - @Platy</i>

## Category
Crypto

## Question
>Alice has just learnt about encryption and OTPs in Applied Cryptography. Now she wants to put her knowledge to the test. She successfully implemented OTPs in her Java code, but the lecturer said that it is insecure.

### Hint
She did not fully understand that 'OT' in 'OTP' stands for 'One-Time'

## Setup Guide
Compile `OTP.java` and run in generate directory (I have no idea how to javac packages)

## Distribution
Zip file
- Java Source Code
	- OTP.java
- Java Serialisation Data
	- output

## Solution
Starting off, the number of possible keys generated is `2 ^ (8 * 30)` which is `1766847064778384329583297500742918515827483896875618958121606201292619776`.
Brute force is definitely not an option.

Looking at the source code, we can see that the generated OTP was used twice
```java
byte[] otp = otp_gen(); // Generating one time pad for the first time!
/*
Code
*/
byte[] data1 = encrypt(text.getBytes(), otp);
byte[] data2 = encrypt(flag.getBytes(), otp);
```

And the method of encryption is using XOR.

```java
public static byte[] encrypt(byte[] data, byte[] key) {
	byte[] encrypted = new byte[data.length];
	for (int i = 0; i < data.length; i++) {
		encrypted[i] = (byte) (data[i] ^ key[i % key.length]);
	}
	return encrypted;
}
```
Since we know that the same key is used to encrypt both data using XOR, and we know one of the 2 data encrypted, we can decrypt the flag!

Formula to decrypt is `(key ^ data) ^ (key ^ flag) ^ data = flag`

So we can rewrite an exploit to decrypt it.
```java
for (int i = 0; i < data1.length; i++) {
	decrypted[i] = (byte) (data1[i] ^ data2[i] ^ textInBytes[i]);
}
System.out.println("Flag: " + new String(decrypted));
```

Working solution `OTP_Break.java` in solution directory

### Flag
`GCTF{p4ds_u53d_0n3_700_m4ny_71m35}`

## Credits
AlexCTF 2017

Crypto

CR2 Many time secrets - 100pts

## Recommended Reads
- https://crypto.stackexchange.com/questions/32795/how-vulnerable-is-the-one-time-pad-otp-encryption-if-the-otp-is-used-twice-w
