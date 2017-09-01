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
