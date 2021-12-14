package lib.resturant;

public class Customer {
    private int id;
    private String name;
    private String shippingAddress;
    private String phone;
    public Customer(int id, String name, String shippingAddress, String phone) {
        this.id = id;
        this.name = name;
        this.shippingAddress = shippingAddress;
        this.phone = phone;
    }
    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public String getShippingAddress() {
        return shippingAddress;
    }
    public void setShippingAddress(String shippingAddress) {
        this.shippingAddress = shippingAddress;
    }
    public String getPhone() {
        return phone;
    }
    public void setPhone(String phone) {
        this.phone = phone;
    }
    // @Override
    // public String toString() {
    //     return "Customer [id=" + id + ", name=" + name + ", phone=" + phone + ", shippingAddress=" + shippingAddress
    //             + "]";
    // }

    
}