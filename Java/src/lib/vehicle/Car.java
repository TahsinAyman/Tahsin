package lib.vehicle;

public class Car extends Vehicle {
	String trans;
	
    public Car(String trans, String name) {
		super(name);
		this.trans = trans;
	}

    
	public Car(int speed, String name, String trans) {
		super(speed, name);
		this.trans = trans;
	}

	@Override
	public String toString() {
		return "Car{" +
				"trans='" + trans + '\'' +
				'}';
	}
}
