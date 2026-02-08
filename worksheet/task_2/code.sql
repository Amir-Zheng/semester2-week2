SELECT customer_name, SUM(price) as total_spent 
FROM customers 
JOIN tickets on customers.customer_id=tickets.customer_id
GROUP BY customers.customer_id
ORDER BY total_spent DESC
LIMIT 5;