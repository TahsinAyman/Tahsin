package lib.hacker_rank;

import java.util.Scanner;

public class HackerRankPractice1 {
    public HackerRankPractice1() {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();

        if (n > 1 && n < 100) {
            if (n % 2 != 0) {
                System.out.println("Weird");
            } else if (n % 2 == 0 && n >= 2 && n <= 5) {
                System.out.println("Not Weird");
            } else if (n % 2 == 0 && n >= 6 && n <= 10) {
                System.out.println("Weird");
            } else if (n % 2 == 0 && n > 20) {
                System.out.println("Not Weird");
            }
        }
    }
}