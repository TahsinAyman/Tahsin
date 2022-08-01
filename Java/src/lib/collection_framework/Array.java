package lib.collection_framework;


import java.util.ArrayList;
import java.util.List;

public class Array {
    public static void main(String[] args) {
        List<Parent> list = new ArrayList<>();
        Parent parent = new Parent("Tahsin", 12);
        list.add(parent);
        Child child = new Child("Ayman", 20);
        list.add(child);
        list.get(0).setAge(22);
        System.out.println(list);
    }
}
