package lib;

public class Delay {
    public Delay() {

    }
    public Delay(long millSecond) {
        try {
            Thread.sleep(millSecond);
        } catch (InterruptedException e) {
            System.out.println("Error the parameter should be long");
        }
    }
    public void delay(long millSecond) {
        try {
            Thread.sleep(millSecond);
        } catch (InterruptedException e) {
            System.out.println("Error the parameter should be long");
        }
    }
}
