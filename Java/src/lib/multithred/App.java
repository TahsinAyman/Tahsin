package lib.multithred;

public class App {
    public static void main(String[] args) {
        for (int i = 0; i < 5; i++) {
            MultiThread multiThread = new MultiThread(5);
            Thread thread = new Thread(multiThread);
            thread.start();
            try {
                thread.join();
            } catch (InterruptedException ie) {

            }
            System.out.println(thread.isAlive());
        }
    }
}