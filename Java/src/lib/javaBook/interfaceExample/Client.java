package lib.javaBook.interfaceExample;

public class Client implements Callback {
    @Override
    public void callback(int p) {
        System.out.println("callback called with " + p);
    }
}
