import java.io.*;
import javax.crypto.*;

public class Solution {
    public static void main(String[] args) throws Exception {
        FileInputStream fileIn = new FileInputStream("output");
        ObjectInputStream inputStream = new ObjectInputStream(fileIn);
        Data dataObject = (Data) inputStream.readObject();
        inputStream.close();

        SealedObject encryptedObject = dataObject.getSealed();
        SecretKey desKey = dataObject.getKey();
        Cipher cipher = Cipher.getInstance("DES/ECB/PKCS5Padding");
        cipher.init(Cipher.DECRYPT_MODE,desKey);
        Flag data = (Flag)encryptedObject.getObject(cipher);

        System.out.println(data.getFlag());
    }
}
