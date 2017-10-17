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
