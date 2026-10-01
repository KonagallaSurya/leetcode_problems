select c.name as Customers from
customers c
LEFT JOIN
orders o
on c.id=o.customerId
WHERE o.id IS NULL;