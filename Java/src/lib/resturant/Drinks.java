package lib.resturant;

public class Drinks extends Item {
    private String brand;
    public Drinks(int id, String itemName, double itemPrice, String brand) {
        super(id, itemName, itemPrice);
        this.brand = brand;
    }
    public String getBrand() {
        return brand;
    }
    public void setBrand(String brand) {
        this.brand = brand;
    }
    @Override
    public String toString() {
        return "Drinks [brand=" + brand + "]";
    }
    
    
}
