package lib.interfacePractice;

import lib.employee.Employee;

public class Tahsin extends Employee implements Programmer , Student {
    
    public Tahsin(String name, String religion, int age, double height, double weight, String gender, int id,
            int salary, int bonus, String work) {
        super(name, religion, age, height, weight, gender, id, salary, bonus, work);
    }
    public Tahsin() {
        
    }

    @Override
    public void certificate() {
        System.out.println("\nThis is my certificate...");
    }
    @Override
    public void experience() {
        System.out.println("\nI worked at Integrate L.T.D");
    }
    @Override
    public void programmingLanguage() {
        System.out.println("\nI know "  + " Programming Language");
    }
    @Override
    public void code() {
        System.out.printf("Code below\n\n");
        System.out.printf("package root;\n\n");
        System.out.printf("public class App {\n");
        System.out.printf("\tpublic static void main(String [] args) {\n");
        System.out.printf("\t\tSystem.out.println(\"This is a sample of a Programm\");\n");
        System.out.printf("\t}\n");
        System.out.printf("}\n");
    }

    @Override
    public void studemtClass() {
        System.out.println("I am in Class 6");        
    }
    @Override
    public void studentId() {
        System.out.println("My Id is 1");
    }
    @Override
    public void studentRoll() {
        System.out.println("My roll is 491");
    }
    @Override
    public void studentHallNumber() {
        System.out.println("207");
    }
}
