SELECT 
	o.order_id,
    c.first_name,
    c.last_name,
    sh.name AS shipper,
    os.name
FROM orders o
INNER JOIN customers c
	USING(customer_id)
INNER JOIN shippers sh
	USING (shipper_id)
INNER JOIN order_statuses os
	ON o.status = os.order_status_id
ORDER BY o.order_id;

-- Order Table Query
-- Finished

SELECT 
	o.order_id,
    c.first_name,
    c.last_name,
    p.name AS product,
    oi.quantity,
    oi.unit_price,
    oi.quantity * oi.unit_price AS toial_price,
    sh.name AS shipper,
    os.name AS status
FROM order_items oi
INNER JOIN products p
	ON oi.product_id = p.product_id
INNER JOIN orders o
	ON oi.order_id = o.order_id
INNER JOIN customers c
	ON o.customer_id = c.customer_id
LEFT OUTER JOIN shippers sh
	ON o.shipper_id = sh.shipper_id
INNER JOIN order_statuses os
	ON o.status = os.order_status_id
ORDER BY oi.order_id;
    
-- Invoice with details


SELECT 
	o.order_id,
    c.first_name,
    c.last_name,
    sum(oi.quantity * oi.unit_price) AS toial_price,
    os.name AS status
FROM order_items oi
INNER JOIN products p
	USING (product_id)
INNER JOIN orders o
	USING (order_id)
INNER JOIN customers c
	ON o.customer_id = c.customer_id
INNER JOIN shippers sh
	ON o.shipper_id = sh.shipper_id
INNER JOIN order_statuses os
	ON o.status = os.order_status_id
GROUP BY c.customer_id
ORDER BY oi.order_id;

-- Payment Invoice
