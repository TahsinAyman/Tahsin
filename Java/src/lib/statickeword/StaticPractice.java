package lib.statickeword;

public class StaticPractice {
    public int id;
    public static String name;
    public static final String city;

    static{
        System.out.println("Static block 0");
        StaticPractice.name = "AAA";
        city = "Dhaka";
    }
    public StaticPractice() {
        System.out.println("I am created.");
    }

    public StaticPractice(int id) {
        this.id = id;
    }

    public static String getName() {
        return name;
    }

    public static void setName(String name) {
        StaticPractice.name = name;
    }

    static{
        System.out.println("Static block 1");
    }

    

    @Override
    public String toString() {
        return "StaticPractice [city=" + city + ", id=" + id + "]";
    }



    public static class InnerClass{
        public int roll;
        public InnerClass(int roll){
            this.roll = roll;
            System.out.println("i am in inner class");
        }
        public int getRoll() {
            return roll;
        }
        public void setRoll(int roll) {
            this.roll = roll;
        }
    }
}
