package lib;

import java.util.Scanner;

public class Calculator {
	
	double var1;
	double var2;

	Scanner input = new Scanner(System.in);

	/***
	 * Md Rashed Karim
	 * This is add method
	 * @return sum
	 */
	public double Add() {
		
		double var1;
		double var2;
		double sum = 0;
		
		System.out.print("Enter the Number: ");
		var1 = input.nextDouble();
		
		do{	
			System.out.print("Enter the Number: ");
			var2 = input.nextDouble();
			
			if (var2 == 0) {
				break;
			}	
			
			sum = (var1 = var1 + var2); //var1+=var2
			
		}while(!(var2 == 0));
			
		return sum;
	}

	/***
	 * Tahsin
	 * @return sum
	 */
	public double Sub() {
		
		double var1;
		double var2;
		double sum = 0;
		
		System.out.print("Enter the Number: ");
		var1 = input.nextDouble();
		
		do{	
			System.out.print("Enter the Number: ");
			var2 = input.nextDouble();
			
			if (var2 == 0) {
				break;
			}	
			
			sum = (var1 = var1 - var2); //var1+=var2
			
		}while(!(var2 == 0));
			
		return sum;
	}
	
	public double Multiplication() {
		
		double var1;
		double var2;
		double sum = 0;
		
		System.out.print("Enter the Number: ");
		var1 = input.nextDouble();
		
		do{	
			System.out.print("Enter the Number: ");
			var2 = input.nextDouble();
			
			if (var2 == 0) {
				break;
			}	
			
			sum = (var1 = var1 * var2); //var1+=var2
			
		}while(!(var2 == 0));
			
		return sum;
	}
	
	public double Div() {
		
		double var1;
		double var2;
		double sum = 0;
		
		System.out.print("Enter the Number: ");
		var1 = input.nextDouble();
		
		do{	
			System.out.print("Enter the Number: ");
			var2 = input.nextDouble();
			
			if (var2 == 0) {
				break;
			}	
			
			sum = (var1 = var1 / var2); //var1+=var2
			
		}while(!(var2 == 0));
			
		return sum;
	}
	public Calculator() {
		int c;
		do {			
			System.out.println("1. Addition");
			System.out.println("2. Subtraction");
			System.out.println("3. Multiplication");
			System.out.printf("4. Division\n");
			System.out.println("0. Exit\n");
			
			System.out.print("Enter choice: ");
			
			c = input.nextInt();
			
			if (c == 1) {
				System.out.println(this.Add() + "\n");	
			}else if (c == 2) {			
				System.out.println(this.Sub() + "\n");
			}else if (c == 3) {			
				System.out.println(this.Multiplication() + "\n");
			}else if (c == 4) {
				System.out.println(this.Div() + "\n");			
			}else if (c == 0) {
				break;
			}else {
				System.out.println("Error");
			}	
		}while(!(c == 0));
	}
}
