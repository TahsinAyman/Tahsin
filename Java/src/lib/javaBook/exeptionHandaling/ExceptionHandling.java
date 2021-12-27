package lib.javaBook.exeptionHandaling;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.sql.SQLException;

public class ExceptionHandling {

    public static void method() throws FileNotFoundException {
        FileReader file = new FileReader("C:\\Users\\Anurati\\Desktop\\abc.txt");
        BufferedReader fileInput = new BufferedReader(file);
        //throw new FileNotFoundException("File not found");
    }

    public static void validate(int age) throws RuntimeException {
        if (age < 18) {
            throw new ArithmeticException("Person is not eligible to vote");
        } else {
            System.out.println("Person is eligible to vote!!");
        }
    }

    void m() throws IOException {
        throw new IOException("device error");
    }

    void n() throws IOException {
        try {
            m();
        } catch (IOException ioe) {
            throw new IOException("Server error");
        }
    }

    void p() {
        try {
            n();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public static void checkNum(int num) {
        if (num < 1) {
            throw new ArithmeticException("\nNumber is negative, cannot calculate square");
        } else {
            System.out.println("Square of " + num + " is " + (num * num));
        }
    }

    public static int divideNum(int m, int n) throws ArithmeticException {
        int div = m / n;
        return div;
    }

    public static void throwThrows() throws ArithmeticException{
        System.out.println("inside the method");
        throw new ArithmeticException("Arithmetic Exception");
    }

    public static void fn(){
        int a = 2/0;
    }
    public static void main(String[] args) {
//        try {
//            validate(18);
//        } catch (RuntimeException e) {
//            System.out.println("Exception caught");
//        }

        try {
            new ExceptionHandling().p();
        } catch (Exception e) {
            e.printStackTrace();
        }
//        try {
//            throw new MyException("My Exception");
//        } catch (MyException me) {
//            System.out.println("Caught");
//            System.out.println(me.getMessage());
//        }
//        try {
//            ExceptionHandling eh = new ExceptionHandling();
//            eh.checkNum(3);
//        } catch (Exception e) {
//            System.out.println(e.getMessage());
//        }

//        try {
//            throwThrows();
//        }catch (ArithmeticException e){
//            System.out.println("caught in main()");
//        }
        System.out.println("Rest of the code");
    }
}
