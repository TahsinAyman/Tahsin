package lib.employee;

import lib.Human;

public class Employee extends Human {
    private int id;
    private int salary;
    private int bonus;
    private String work;
    public double aDouble;

    /***
     * An empty Constructor
     */
    public Employee() {
        
    }

    /***
     * A non empty Constructor
     */
    public Employee(String name, String religion, int age, double height, double weight, String gender, int id,
            int salary, int bonus, String work) {
        super(name, religion, age, height, weight, gender);
        this.id = id;
        this.salary = salary;
        this.bonus = bonus;
        this.work = work;
    }

    /***
     * Getter of 'getBonus'
     */
    public int getBonus() {
        return bonus;
    }
    public void setBonus(int Bonus) {
        this.bonus = Bonus;
    }
    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public int getSalary() {
        return salary;
    }
    public void setSalary(int Salary) {
        this.salary = Salary;
    }
    public void setWork(String work) {
        this.work = work;
    }
    public String getWork() {
        return work;
    }

    @Override
    public String toString() {
        return super.toString() + "[Work: " + work +"]\n[ID: " + id + "]\n[Salary: " + salary
                + "]\n[Bonus: " + bonus + "]\n";
    }
}
