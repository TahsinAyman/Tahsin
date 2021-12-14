package lib.resturant;

public class OrderLine {
    private int id;
    private Item item;
    private int quantity;
    private double unitPrice;
    public OrderLine(int id, Item item, int quantity, double unitPrice) {
        this.id = id;
        this.item = item;
        this.quantity = quantity;
        this.unitPrice = unitPrice;
    }
    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public Item getItem() {
        return item;
    }
    public void setItem(Item item) {
        this.item = item;
    }
    public int getQuantity() {
        return quantity;
    }
    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public double getUnitPrice() {
        return unitPrice;
    }
    public void setUnitPrice(double unitPrice) {
        this.unitPrice = unitPrice;
    }
    @Override
    public String toString() {
        return "OrderLine [id=" + id + ", item=" + item + ", quantity=" + quantity + ", unitPrice=" + unitPrice + "]";
    }

    
}
