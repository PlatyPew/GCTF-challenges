package Time_to_Crypt;

import java.io.*;
import java.util.*;

public class OTP {

    static class Data implements Serializable {

        private final byte[] data1;
        private final byte[] data2;

        public Data(byte[] data1, byte[] data2) {
            this.data1 = data1;
            this.data2 = data2;
        }
        
        public byte[] getData1() {
            return this.data1;
        }
        
        public byte[] getData2() {
            return this.data2;
        }
    }

    public static byte[] otp_gen() {
        Random randomno = new Random();
        byte[] nbyte = new byte[30];
        randomno.nextBytes(nbyte);
        return nbyte;
    }

    public static byte[] encrypt(byte[] data, byte[] key) {
        byte[] encrypted = new byte[data.length];
        for (int i = 0; i < data.length; i++) {
            encrypted[i] = (byte) (data[i] ^ key[i % key.length]);
        }
        return encrypted;
    }

    public static void main(String[] args) throws Exception {
        byte[] otp = otp_gen(); // Generating one time pad for the first time!

        String flag = "GCTF{XXXXXXXXXXXXXXXXXXXXXXXXXXXX}"; // Flag goes here!
        String text = "Congratulations! Here is the flag!";
        
        int lengthOfInput = text.length();
        if (flag.length() != lengthOfInput) {
            System.out.println("Length of input must be " + lengthOfInput);
            return;
        }
        
        byte[] data1 = encrypt(text.getBytes(), otp);
        byte[] data2 = encrypt(flag.getBytes(), otp);
        Data data = new Data(data1, data2);

        FileOutputStream f = new FileOutputStream("output"); // Output of file
        ObjectOutputStream o = new ObjectOutputStream(f);
        o.writeObject(data);
        o.close();
    }
}
