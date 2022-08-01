SELECT 
	i.invoice_id,
    i.number,
    i.invoice_total,
    i.payment_total,
    c.name AS client,
    c.address,
    c.phone
FROM invoices i
INNER JOIN clients c
	USING (client_id)
ORDER BY i.invoice_id;

-- Invoices Query 

SELECT 
	p.payment_id,
    c.name,
    c.phone,
    i.number,
    i.invoice_total,
    i.payment_total,
    p.amount,
    p.date,
    pm.name AS payment
FROM payments p
INNER JOIN invoices i
	ON p.invoice_id = i.invoice_id
INNER JOIN clients c
	ON p.client_id = c.client_id
INNER JOIN payment_methods pm
	ON p.payment_method = pm.payment_method_id;

-- Payments Query