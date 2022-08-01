SELECT * FROM employees
WHERE reports_to IS NULL;

-- Manager Query

SELECT * FROM employees 
WHERE reports_to IS NOT NULL;

-- Employee Query

SELECT 
	e.employee_id,
    e.first_name,
    e.last_name,
    e.job_title,
    e.salary,
    o.address,
    o.city,
    o.state
FROM employees e
INNER JOIN offices o
	ON e.office_id = o.office_id
WHERE e.reports_to IS NOT NULL;

-- Offices Of Employee Query


SELECT 
	e.employee_id,
    e.first_name,
    e.last_name,
    e.job_title,
    e.salary,
    o.address,
    o.city,
    o.state
FROM employees e
INNER JOIN offices o
	ON e.office_id = o.office_id
WHERE e.reports_to IS NULL;


-- Offices of Manager Query