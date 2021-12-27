package lib.vendorexam;


import lib.vehicle.Car;

import java.util.StringTokenizer;

public class VendorExam {

    public static void main(String[] args) {
        StringTokenizer st = new StringTokenizer("rashed karim,Abdullah Al Adib,Tahsin Noob");
        // printing next token
        System.out.println(st.nextToken());
    }
}