package lib.javaBook.exeptionHandaling;

public class ExeptionHandaling {
    public ExeptionHandaling() {
        int x;
        int y;

        try {
            x = 0;
            y = 99 / x;
        } catch(ArithmeticException e) {
            System.out.println("Division by zero");
        }

        System.out.println("VS");

        int a;
        int b;

        a = 0;
        b = 99 / a;

    }
}
