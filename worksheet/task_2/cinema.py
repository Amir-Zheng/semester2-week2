"""
This is where you should write your code and this is what you need to upload to Gradescope for autograding.

You must NOT change the function definitions (names, arguments).

You can run the functions you define in this file by using test.py (python test.py)
Please do not add any additional code underneath these functions.
"""

import sqlite3


def customer_tickets(conn, customer_id):
    """
    Return a list of tuples:
    (film_title, screen, price)

    Include only tickets purchased by the given customer_id.
    Order results by film title alphabetically.
    """

    return_list=[]
    query=  '''
            SELECT title, screen, price 
            FROM customers 
            JOIN tickets on customers.customer_id=tickets.customer_id
            JOIN screenings on tickets.screening_id=screenings.screening_id
            JOIN films on screenings.film_id=films.film_id
            WHERE customers.customer_id=?
            ORDER BY title ASC;
            '''
    
    cursor = conn.execute(query,(customer_id,))
    for row in cursor:
        film_title=row[0]
        screen=row[1]
        price=row[2]
        return_list.append((film_title, screen, price))
    
    return return_list


def screening_sales(conn):
    """
    Return a list of tuples:
    (screening_id, film_title, tickets_sold)

    Include all screenings, even if tickets_sold is 0.
    Order results by tickets_sold descending.
    """
    return_list=[]
    query=  '''
            SELECT screenings.screening_id, title, COUNT(ticket_id) as tickets_sold  
            From screenings
            LEFT JOIN tickets on screenings.screening_id=tickets.screening_id
            LEFT JOIN films on screenings.film_id=films.film_id
            GROUP BY screenings.screening_id
            ORDER BY tickets_sold DESC;
            '''
    
    cursor = conn.execute(query)
    for row in cursor:
        screening_id=row[0]
        film_title=row[1]
        tickets_sold=row[2]
        return_list.append((screening_id, film_title, tickets_sold))
    
    return return_list


def top_customers_by_spend(conn, limit):
    """
    Return a list of tuples:
    (customer_name, total_spent)

    total_spent is the sum of ticket prices per customer.
    Only include customers who have bought at least one ticket.
    Order by total_spent descending.
    Limit the number of rows returned to `limit`.
    """

    return_list=[]
    query=  '''
            SELECT customer_name, SUM(price) as total_spent 
            FROM customers 
            JOIN tickets on customers.customer_id=tickets.customer_id
            GROUP BY customers.customer_id
            ORDER BY total_spent DESC
            LIMIT ?;
            '''
    
    cursor = conn.execute(query,(limit,))
    for row in cursor:
        customer_name=row[0]
        total_spent=row[1]
        return_list.append((customer_name, total_spent))
    
    return return_list