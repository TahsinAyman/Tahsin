package lib.vendorexam.tools;

import lib.vendorexam.Exportable;

public class Tools implements Exportable {
    public static String name;
    public int i;
    public void export() {
        System.out.println("Tools");
    }
    public static String getTools(){
        return "Green";
    }
    public String getTool(){
        return "Red";
    }
}
