package lib.interfacePractice;

import lib.employee.Employee;

public class DoctorPolash extends Employee implements Doctor , Driver {

    private int visitRate;

    public DoctorPolash() {
        
    }

    public DoctorPolash(String name, String religion, int age, double height, double weight, String gender, int id,
            int salary, int bonus, String work, int visitRate) {
        super(name, religion, age, height, weight, gender, id, salary, bonus, work);
        this.visitRate = visitRate;
    }

    public void setVisitRate(int visitRate) {
        this.visitRate = visitRate;
    }
    public int getVisitRate() {
        return visitRate;
    }

    @Override
    public void operation() {
        System.out.println("This is a sample of a Operation");
    }
    @Override
    public void prespriction() {
        System.out.println("This is a sample of a Perspriction");
    }
    @Override
    public void drive() {
        System.out.println("I can drive");        
    }
}
