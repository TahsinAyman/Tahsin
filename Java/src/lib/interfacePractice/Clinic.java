package lib.interfacePractice;

public class Clinic {
    public void treatment(Doctor doctor) {
        doctor.operation();
        doctor.prespriction();
    }
    public void homeServiceTreatment(Doctor doctor, Driver driver) {
        driver.drive();
        doctor.prespriction();
    } 
}
