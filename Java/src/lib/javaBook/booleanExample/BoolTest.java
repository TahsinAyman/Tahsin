package lib.javaBook.booleanExample;

public class BoolTest {
    public BoolTest() {
        boolean b;

        b = false;
        System.out.println("b is " + b);

        b = true;
        System.out.println("b is " + b);

        if(b) {
            System.out.println("This is executated");
        }

        b = false;

        if(b == false) {
            System.out.println("This is not Executed");
        }
        
        System.out.println("10 > 9 is " + (10 > 9));
    }
}
