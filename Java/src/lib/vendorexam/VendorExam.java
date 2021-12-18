package lib.vendorexam;

import java.util.ArrayList;
import java.util.List;

public class VendorExam {

    public static void main(String[] args) {
        Student [] students = new Student[3];
        students[0] = new Student("Tah", 12);
        students[1] = new Student("AAA", 19);

        for (Student student: students          ) {
            System.out.println(""+ student.name);
        }
    }
}