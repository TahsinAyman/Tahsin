package lib.javaBook.generics;

public class IntegerPrinter<Tahsin> {
    Tahsin i;

    public IntegerPrinter(Tahsin i) {
        this.i = i;
    }

    public void show(){
        System.out.println(i);
    }
}
