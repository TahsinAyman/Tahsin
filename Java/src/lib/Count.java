package lib;

public class Count {
    private static int count = 0;

    public Count() {
        count++;
        System.out.println(count);
    }
}
