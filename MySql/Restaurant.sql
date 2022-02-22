use resturant;

insert into sales_details (item_id, sales_id, unit_price, quantity) values
(9, 2, 15, 20),(10, 2, 40, 20);

commit;

SELECT 
s.id Sales_ID, Sales_date,
Customer_id, Customer_Name, c.phone
FROM sales_main as s 
INNER JOIN customer as c on c.id = s.customer_id
where s.id = 1;

SELECT 
sd.Sales_ID,  
sd.Item_id, i.Item_Name, 
sd.id, sd.quantity, sd.unit_price
FROM sales_details sd INNER JOIN item i on i.id = sd.Item_id
where sd.Sales_ID = 1;

SELECT 
s.id Sales_ID, Sales_date,
Customer_id, Customer_Name, c.phone,  
sd.Item_id, i.Item_Name, 
sd.id, sd.quantity, sd.unit_price
FROM sales_main as s 
INNER JOIN customer as c on c.id = s.customer_id
INNER JOIN sales_details sd on sd.Sales_id = s.id
INNER JOIN item i on i.id = sd.Item_id
where s.id = 1;

select * from customer;
select * from item;
select * from sales_main;
select * from sales_details;
