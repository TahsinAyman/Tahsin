package lib.resturant;

public class Pizza extends Item {
   
    private String toppings;

    public Pizza(int id, String itemName, double itemPrice, String toppings) {
        super(id, itemName, itemPrice);
        this.toppings = toppings;
    }

    public String getToppings() {
        return toppings;
    }

    public void setToppings(String toppings) {
        this.toppings = toppings;
    }

    @Override
    public String toString() {
        return "Pizza [toppings=" + toppings + "]";
    }
    
}
