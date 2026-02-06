SELECT AVG(quantity) FROM orders 
FULL JOIN order_items on orders.order_id = order_items.order_id;