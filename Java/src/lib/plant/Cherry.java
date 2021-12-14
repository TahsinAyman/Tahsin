package lib.plant;

public class Cherry extends Plant {

    public Cherry() {
        //Implicit Constructor if there is no Paramiters in the Main class
    }

    public Cherry(Double height, String name, String leafColor, double branchThikness) {
        super(height, name, leafColor, branchThikness);
    }

    @Override
    public String toString() {
        return super.toString();
    }
}
