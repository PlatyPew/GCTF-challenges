# Depresso Espresso
Reverse Engineering Java code

<i>Creator - @Platy</i>

## Category
Reversing

## Question
>I've intercepted 2 files. One file is a Java class while the other is apparently the output of the Java program. I've been trying to work out how to use the program but it constantly gives me an error. I've dranked countless cups of java, but I'm still stuck. Help me please!

### Hint
Feistel. Just Feistel.

## Setup
Do `make all` in generate directory

## Distribution
Zip file `MD5: 046eb2455d042de7b8af0556e160cbed`
- Depresso Espresso.zip
	- Compiled Java Class Data
		- Lolwhut.class
		- Data.class
		- Flag.class
	- Java Serialization Data
		- output

## Solution
Upon decompiling the files with some external programs such as [JD-Gui](http://jd.benow.ca/), we can retrieve the original source code.
```java
import java.io.FileOutputStream;
import java.io.ObjectOutputStream;
import java.io.PrintStream;
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SealedObject;
import javax.crypto.SecretKey;

public class Lolwhut {
  public static void main(String[] paramArrayOfString) throws Exception {
    if (paramArrayOfString.length != 4) {
      System.out.println("Lolwhut <algorithm> <cipher mode> <flag> <output file>");
      return;
    }
    KeyGenerator localKeyGenerator = KeyGenerator.getInstance(paramArrayOfString[0]);
    SecretKey localSecretKey = localKeyGenerator.generateKey();
    Cipher localCipher = Cipher.getInstance(paramArrayOfString[1]);
    localCipher.init(1, localSecretKey);
    SealedObject localSealedObject = new SealedObject(new Flag(paramArrayOfString[2]), localCipher);
    Data localData = new Data(localSealedObject, localSecretKey);
    FileOutputStream localFileOutputStream = new FileOutputStream(paramArrayOfString[3]);
    ObjectOutputStream localObjectOutputStream = new ObjectOutputStream(localFileOutputStream);
    localObjectOutputStream.writeObject(localData);
    localObjectOutputStream.close();
    System.out.println("File " + paramArrayOfString[3] + " created");
  }
}
```
The program takes in 4 arguments, the encryption algorithm, cipher mode, flag and the file to output.

Reading the code, we see that the program uses an encryption algorithm with a cipher mode. However, how do we know what the original program uses? By using `strings output`, we can get all of the 
```
java.security.KeyRep$Type
java.lang.Enum
SECRETsr
javax.crypto.SealedObject>6=
encodedParamsq
encryptedContentq
	paramsAlgq
sealAlgq
xppuq
DES/ECB/PKCS5Padding
```
The algorithm is `DES` and the cipher mode is `DES/ECB/PKCS5Padding`. With this information, we are one step closer to solving this challenge.

Now all we have left to do is to extract out the key and data from the file, use the key to decrypt the flag object and to get the flag.

Working solution in solution directory.

### Flag
`GCTF{d35_l0v35_4_6r347_c1ph3r}`

## Credits
- https://github.com/java-decompiler/jd-gui

## Recommended Reads
None.
