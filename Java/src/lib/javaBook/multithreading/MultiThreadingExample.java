package lib.javaBook.multithreading;

public class MultiThreadingExample implements Runnable {
    public MultiThreadingExample() {
        Thread thread1 = new Thread("Tahsin");
        Thread thread2 = new Thread("Ayman");

        thread2.start();
        thread1.start();

        System.out.print(thread1.getName());

        for (int i = 1; i <= 10; i++) {
            System.out.println(i);
        }

        System.out.print(thread2.getName());
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void run() {

    }
}