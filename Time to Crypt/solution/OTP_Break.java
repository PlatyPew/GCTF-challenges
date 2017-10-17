package Time_to_Crypt;

import Time_to_Crypt.OTP.Data;
import java.io.*;

public class OTP_Break {

    public static void crack(byte[] data1, byte[] data2) {
        byte[] textInBytes = "Congratulations! Here is the flag!".getBytes();
        byte[] decrypted = new byte[data1.length];
        if (data1.length == data2.length) {
            for (int i = 0; i < data1.length; i++) {
                decrypted[i] = (byte) (data1[i] ^ data2[i] ^ textInBytes[i]);
            }
            System.out.println("Flag: " + new String(decrypted));
        }
    }

    public static void main(String[] args) throws Exception {
        FileInputStream f = new FileInputStream("output");
        ObjectInputStream o = new ObjectInputStream(f);
        Data data = (Data) o.readObject();
        crack(data.getData1(), data.getData2());
    }
}
