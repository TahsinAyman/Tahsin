package lib.resturant;

public abstract class Item {
    private int id;
    private String itemName;
    private double itemPrice;
    public Item(int id, String itemName, double itemPrice) {
        this.id = id;
        this.itemName = itemName;
        this.itemPrice = itemPrice;
    }

    
    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public String getItemName() {
        return itemName;
    }
    public void setItemName(String itemName) {
        this.itemName = itemName;
    }
    public double getItemPrice() {
        return itemPrice;
    }
    public void setItemPrice(double itemPrice) {
        this.itemPrice = itemPrice;
    }
    @Override
    public String toString() {
        return "Item [id=" + id + ", itemName=" + itemName + ", itemPrice=" + itemPrice + "]";
    }

    
}
