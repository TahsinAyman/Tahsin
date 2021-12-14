package lib.vendorexam;


import java.nio.channels.ScatteringByteChannel;
import java.util.ArrayList;
import java.util.List;

public class VendorExam {
    public static void main(String[] args) {

        String [] names = {"Thomas", "Peter", "Joseph"};
        String [] opt = new String[3];
        int i = 0;
        try {
            for (String n :
                    names) {
                opt[i] = n.substring(2, 6);
                i++;
            }
        }catch(Exception e){
            opt[i] = "Invalid";
        }

        for (String s :
                opt) {
            System.out.println(s);
        }

    }
}
