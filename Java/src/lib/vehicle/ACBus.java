package lib.vehicle;

public class ACBus extends Bus{
    public ACBus(String name) {
        super(name);
    }

    @Override
    public String toString() {
        return "ACBus{" +
                "name='" + name + '\'' +
                '}';
    }
}
