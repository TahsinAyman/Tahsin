package lib.collection_framework;

public class Parent {
    private String name;
    private int age;

    public Parent() {

    }
    public Parent(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return this.age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String toString() {
        return "{\"name\": \"" + this.name + "\",\"Age\": " + this.age + "}";
    }
}
