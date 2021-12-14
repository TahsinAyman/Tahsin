package lib.designpattern.singleton;

public class Company {
    private static Company obj;
    public static int id;
    public String name;

    private Company() {

    }

    public static Company getObj() {
        if (obj == null) {
            synchronized (Company.class) {
                if (obj == null) {
                    obj = new Company();
                }
            }
        }
        return obj;
    }

    public void show() {
        System.out.println("Yes");
    }
}
