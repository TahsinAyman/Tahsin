package lib.plant;

public class Mango extends Plant {

    public Mango() {
        //Implicit Constructor if there is no Paramiters in the Main class   
    }

    public Mango(double height, String name, String leafColor, double branchThikness) {
        super(height, name, leafColor, branchThikness);
    }

    @Override
    public String toString() {
        return super.toString();
    }
}
