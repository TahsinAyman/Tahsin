package lib.generics;

public class Print {
    public static void main(String []args) {
        Printer<String> printer = new Printer<>("tahsin ayman");
        System.out.println(printer.print());
    }
}