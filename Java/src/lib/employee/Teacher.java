package lib.employee;

public class Teacher extends Employee {

    public Teacher(String name, String religion, int age, double height, double weight, String gender, int id,
            int salary, int bonus, String work) {
        super(name, religion, age, height, weight, gender, id, salary, bonus, work);
    }

    @Override
    public String toString() {
        return super.toString();
    }
}
