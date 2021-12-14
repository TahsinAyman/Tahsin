package lib;

public class Meat extends Food {

	@Override
	public Meat get() {
		return this;
	}

	public void message() {
		System.out.println("welcome to covariant return type");
	}

	
	public Float add(int a, int b) {
		return (float) (a + b);
	}
}
