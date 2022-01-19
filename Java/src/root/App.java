package root;

import lib.javaBook.collections.Book;

import java.util.*;

public class App {
    public static void main(String[] args) {
        HashSet<String> hashSet = new HashSet<String>();

        long start = System.currentTimeMillis();
        for (int i = 0; i < 900000; i++) {
            hashSet.add(String.valueOf(i));
        }

        System.out.println("Insert HashSet Time: " + (System.currentTimeMillis() - start));


        ArrayList<String> arrayList = new ArrayList<String>();

        start = System.currentTimeMillis();

        for (int i = 0; i < 900000; i++) {
            arrayList.add(String.valueOf(i));
        }
        System.out.println("Insert ArrayList Time: " + (System.currentTimeMillis() - start));

        LinkedList<String> linkedList = new LinkedList<String>();

        start = System.currentTimeMillis();

        for (int i = 0; i < 900000; i++) {
            linkedList.add(String.valueOf(i));
        }
        System.out.println("Insert linkedList Time: " + (System.currentTimeMillis() - start));

        TreeSet<String> treeSet = new TreeSet<String>();

        start = System.currentTimeMillis();

        for (int i = 0; i < 900000; i++) {
            treeSet.add(String.valueOf(i));
        }
        System.out.println("Insert TreeSet Time: " + (System.currentTimeMillis() - start));

        PriorityQueue<String> priorityQueue = new PriorityQueue<>();

        start = System.currentTimeMillis();

        for (int i = 0; i < 900000; i++) {
            priorityQueue.add(String.valueOf(i));
        }
        System.out.println("Insert priorityQueue Time: " + (System.currentTimeMillis() - start));

        HashMap hashMap = new HashMap();

        start = System.currentTimeMillis();

        for (int i = 0; i < 900000; i++) {
            hashMap.put(String.valueOf(i), String.valueOf(i));
        }
        System.out.println("Insert hashMap Time: " + (System.currentTimeMillis() - start));
    }
}