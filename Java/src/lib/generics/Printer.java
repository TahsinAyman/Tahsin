package lib.generics;

public class Printer<T> {
    private T t;

    public T print() {
        return this.t;
    }

    public Printer(T t) {
        this.t = t;
    }
}