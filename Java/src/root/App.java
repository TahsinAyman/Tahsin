package root;

import lib.Delay;

import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        new App().getch();
        System.out.println("ok");
    }

    public void getch() {
        Scanner kb = new Scanner(System.in);

        boolean pressed = false;
        String entered = "";
        while (!pressed) {
            entered = kb.next();
            if (entered.equals("")) {
                pressed = true;
            }
        }
    }
}