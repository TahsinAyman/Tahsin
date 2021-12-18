package lib.javaBook.exeptionHandaling;

public class Finalize {
    public static void main(String[] args) {
        Finalize obj = new Finalize();
        System.out.println(obj.hashCode());
        obj = null;
        System.gc();
        System.out.println("End of garbase collection");
    }

    protected void finalize(){
        System.out.println("finalize method called");
    }
}
