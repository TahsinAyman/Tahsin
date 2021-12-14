package lib.resturant;

import java.util.Date;
import java.util.List;

public class Order {
    private int id;
    private Date orderDate;
    private Customer customer;
    private List<OrderLine> orderLines;
    public Order(int id, Date date, Customer customer, List<OrderLine> orderLines) {
        this.id = id;
        this.orderDate = date;
        this.customer = customer;
        this.orderLines = orderLines;
    }
    
    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public Date getOrderDate() {
        return orderDate;
    }
    public void setOrderDate(Date orderDate) {
        this.orderDate = orderDate;
    }
    public Customer getCustomer() {
        return customer;
    }
    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
    public List<OrderLine> getOrderLines() {
        return orderLines;
    }
    public void setOrderLines(List<OrderLine> orderLines) {
        this.orderLines = orderLines;
    }
    @Override
    public String toString() {
        return "Order [customer=" + customer + ", id=" + id + ", orderDate=" + orderDate + ", orderLines=" + orderLines
                + "]";
    }
    
    
}
