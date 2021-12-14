package lib;

import java.util.Scanner;

public class MethodOverloading {

	public Scanner input = new Scanner(System.in);
	public int integer;
	
	public void overload(double i) {
		System.out.println("Overload: " + i);
	}
	
	public void oveload(int i) {
		System.out.println("Overload: " + i);
	}
	
	public void overload() {
		System.out.printf("Overload: ");
		integer = input.nextInt();
		System.out.println(integer);
	}
}
