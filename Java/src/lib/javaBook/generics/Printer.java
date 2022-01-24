package lib.javaBook.generics;

import lib.vehicle.Bus;
import lib.vehicle.Vehicle;

import java.util.List;

public class Printer<Type extends Vehicle> {
    Type i;

    public Printer(Type i) {
        this.i = i;
    }

    public void display(List<? super Bus> vList){
        for(Object v: vList){
            System.out.println(v);
        }
    }

    public void show(){
        System.out.println(i);
    }
}
