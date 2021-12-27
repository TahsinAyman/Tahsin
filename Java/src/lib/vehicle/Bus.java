package lib.vehicle;

public class Bus extends Vehicle {
    String name;

    public Bus(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "Bus{" +
                "name='" + name + '\'' +
                '}';
    }
}
