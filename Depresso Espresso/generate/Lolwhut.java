import java.io.*;
import javax.crypto.*;
public class Lolwhut {
    public static void main(String[] args) throws Exception {
		if (args.length != 4) {
			System.out.println("Lolwhut <algorithm> <cipher mode> <flag> <output file>");
			return;
		}
        KeyGenerator quack = KeyGenerator.getInstance(args[0]);
        SecretKey keystheyou = quack.generateKey();
        Cipher asdasd = Cipher.getInstance(args[1]);
        asdasd.init(Cipher.ENCRYPT_MODE, keystheyou);
        SealedObject majiks = new SealedObject(new Flag(args[2]),asdasd);
        Data hue = new Data(majiks, keystheyou);
        FileOutputStream lel = new FileOutputStream(args[3]);
        ObjectOutputStream lol = new ObjectOutputStream(lel);
        lol.writeObject(hue);
        lol.close();
	System.out.println("File " + args[3] + " created");
    }
}
