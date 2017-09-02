# Reverse Me
Reverse Engineering Java code

<i>Creator - @Platy</i>

## Category
Bin

## Question
I've intercepted 2 files. One file is a Java class while the other is apparently the output of the Java program. I've been trying to work out how to use the program but it constantly gives me an error. Reverse the program and help me see what the output file is all about.

## Hint
Feistel. Just Feistel.

## Setup
Just distribute files

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

By recompiling the Java source code, we get some errors about not having `Flag` or `Data` which are value beans used to create objects. Once again, we can study `Lolwhut.class` and rewrite those classes.
```java
// Flag.java
import java.io.Serializable;
public class Flag implements Serializable {
    private final String flag;
    public Flag(String flag) {
        this.flag = flag;
    }
    public String getFlag() {
        return this.flag;
    }
}
```
and
```java
// Data.java
import java.io.Serializable;
import javax.crypto.SealedObject;
import javax.crypto.SecretKey;
public class Data implements Serializable {
	private final SealedObject sealed;
	private final SecretKey key;
	public Data(SealedObject sealed, SecretKey key) {
		this.sealed = sealed;
		this.key = key;
	}
	public SealedObject getSealed() {
		return sealed;
	}
	public SecretKey getKey() {
		return key;
	}
}
```
Now all we have left to do is to extract out the key and data from the file, use the key to decrypt the flag object and to get the flag.

Working solution in solution directory.

### Flag
`GCTF{d35_l0v35_4_6r347_c1ph3r}`

## Distribution
Compile Java Class Data
- Lolwhut.class

Java Serialization Data
- output

## Credits
None.