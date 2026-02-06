import sqlite3
# you will need to pip install pandas matplotlib
import pandas as pd
import matplotlib as mpl

def get_connection(db_path="orders.db"):
    """
    Establish a connection to the SQLite database.
    Returns a connection object.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def list_all_product_categories(db:sqlite3.Connection):
    query=  '''
            SELECT category FROM products GROUP BY category;
            '''
    cursor = db.execute(query)
    print('list of all product categories: ')
    for row in cursor:
        print(row[0])

def menu():
    print("1 - Orders overview")
    print("Q - quit")
    choice = -1
    while (choice not in ["1","Q"]):
        choice = input("Enter your choice: ").upper()
    return choice

def orders_overview(db:sqlite3.Connection):
    print("What do you wish to view?")
    print("1 - Total orders")
    print("2 - Orders per category")
    print("3 - Average basket size")
    print("Q - quit")
    choice = -1
    while (choice not in ["1","2","3","Q"]):
        choice = input("Enter your choice: ").upper()
    match choice:
        case "1":
            total_orders(db)
        case "2":
            total_orders_per_category(db)
        case "3":
            average_basket_size(db)

def total_orders(db:sqlite3.Connection):
    query=  '''
            SELECT Count(order_id) FROM orders;
            '''
    cursor = db.execute(query)
    for row in cursor:
        print(row[0])

def total_orders_per_category(db:sqlite3.Connection):
    query=  '''
            SELECT category,Count(orders.order_id) FROM orders 
            FULL JOIN order_items on orders.order_id = order_items.order_id 
            FULL JOIN products on order_items.product_id=products.product_id 
            GROUP BY category;
            '''
    cursor = db.execute(query)
    for row in cursor:
        print(row[0],row[1])

def average_basket_size(db:sqlite3.Connection):
    query=  '''
            SELECT AVG(quantity) FROM orders 
            JOIN order_items on orders.order_id = order_items.order_id;
            '''
    cursor = db.execute(query)
    for row in cursor:
        print(row[0])

def main():

    db = get_connection()
    while 1:
        choice = menu()
        match(choice):
            case "1":
                orders_overview(db)
            case "Q":
                exit()

    db.close()


if __name__=="__main__":
    main()
