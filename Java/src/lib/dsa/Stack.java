package lib.dsa;

import java.util.Arrays;

public class Stack {

	int data[];
	int size;
	int top = -1;
	public Stack(int size) {
		this.size = size;
		this.data = new int[size];
	}
	
	private boolean isFull() {
		if (this.top == this.size)
			return true;
		else
			return false;
	}
	
	private boolean isEmpty() {
		if (this.top == -1)
			return true;
		else
			return false;
	}
	
	public void push(int val) {
		if (! this.isFull()) {
			top += 1;
			data[top] = val;
		}
	}
	
	public int pop() {
		int d = 0;
		if (! this.isEmpty()) {
			d = data[top];
			// data[top] = 0;
			top -= 1;
		}
		return d;
	}
	
	public int peek() {
		if (! this.isEmpty()) {
			return data[top];
		}
		return 0;
	}
	
	
	
	
}
