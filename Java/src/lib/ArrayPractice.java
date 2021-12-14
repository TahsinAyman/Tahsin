package lib;

import java.util.Scanner;

public class ArrayPractice {

    private int rowSize = 2;
    private int colSize = 3;

    public ArrayPractice() {
        System.out.println("-------------------------");
        int t[][] = new int[this.rowSize][this.colSize];
        for (int row = 0; row < this.rowSize; row++) {
            for (int col = 0; col < this.colSize; col++) {
                System.out.print(" * ");
            }
            System.out.print("\n");
        }
        System.out.println("-------------------------");
        System.out.println("    Row Size" + this.rowSize);
        System.out.println("+   Col Size" + this.colSize);
        System.out.println("-------------------------");
        System.out.println(this.rowSize * this.colSize);
        System.out.println("-------------------------");
    }

    public void rowEdit() {
        for (int row = 0; row < this.rowSize; row++) {
            for (int col = 0; col < this.colSize; col++) {
                if (row == 1) {
                    System.out.print("poop ");
                } else {
                    System.out.print(" * ");
                }
            }
            System.out.print("\n");
        }
        System.out.println("-------------------------");
    }
}