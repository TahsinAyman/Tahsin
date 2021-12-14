package lib.resturant;

public class Burger extends Item {
    private String type;

    public Burger(int id, String itemName, double itemPrice, String type) {
        super(id, itemName, itemPrice);
        this.type = type;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    @Override
    public String toString() {
        return "Burger [type=" + type + "]";
    }

}
