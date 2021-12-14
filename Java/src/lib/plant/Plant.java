package lib.plant;

public class Plant {
    private double height;
    private String name;
    private String leafColor;
    private double branchThikness;
    
    public Plant() {
        //Implicit Constructor if there is no Paramiters in the Main class
    }
    public Plant(double height, String name, String leafColor, double branchThikness) {
        this.height = height;
        this.name = name;
        this.leafColor = leafColor;
        this.branchThikness = branchThikness;
    }
    public double getHeight() {
        return height;
    }
    public void setHeight(double height) {
        this.height = height;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public String getLeafColor() {
        return leafColor;
    }
    public void setLeafColor(String leafColor) {
        this.leafColor = leafColor;
    }
    public void setBranchThikness(double branchThikness) {
        this.branchThikness = branchThikness;
    }
    public double getBranchThikness() {
        return branchThikness;
    }

    @Override
    public String toString() {
        return "\nName: " + name + "\nHeight: " + height + 
        "\nLeaf Color: " + leafColor + "\nBranch Thikness: " + branchThikness;
    }    
}