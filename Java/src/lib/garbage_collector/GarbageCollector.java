package lib.garbage_collector;

public class GarbageCollector {
    public static void main(String[] args) {
        Doctor doctor = new Doctor();
        doctor.assist();
        System.gc();
        doctor.assist();
    }
}
