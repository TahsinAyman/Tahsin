package lib.multithred;

public class MultiThreadingExample1 implements Runnable{

    public MultiThreadingExample1() {
        

        Thread myThread = new Thread("Tahsin");
        Thread myThread2 = new Thread("Ayman");
        
        myThread.start();
        myThread2.start();
        
        for (int i = 1; i <= 10; i++) {
            System.out.println(myThread.getName());
        }
        
        System.out.print("\t" + myThread2.getName());
    }

    @Override
    public void run() {

    }
}
