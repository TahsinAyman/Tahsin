package root;

public class App {
    public static void main(String[] args) {
        int count = 0;
        String s1 = "java";
        String s2 = "java";
        StringBuilder s3 = new StringBuilder("java");
        if (s1 == s2) count++;
        if (s1.equals(s2)) count++;
        if (s1.equals(s3)) count++;
        System.out.println(count);
        System.out.println("noob Brother");
    }

}
