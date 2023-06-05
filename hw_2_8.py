import sqlite3

def create_connection(db_hw):
    connection = sqlite3.connect(db_hw)
    return connection

def create_table(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)

sql_create_produkt_table = '''
CREATE TABLE IF NOT EXISTS produkt (
id INTEGER PRIMARY KEY AUTOINCREMENT, 
product_title VARCHAR (200) NOT NULL,
price DOUBLE (10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER (5) NOT NULL DEFAULT 0
);
'''
def create_produkt(conn, produkt: tuple):
    sql = '''INSERT INTO produkt
     (product_title, price, quantity) 
     VALUES (?, ?, ?);'''
    cursor = conn.cursor()
    cursor.execute(sql,produkt)
    conn.commit()

def update_product_quantity(conn, id:int, new_quantity):
    sql = '''UPDATE products SET quantity = ? WHERE id = ?;'''
    cursor = conn.cursor()
    cursor.execute(sql, (new_quantity, id,))
    conn.commit
    

def update_product_price(conn, id:int, new_price):
    sql = '''UPDATE products SET price = ? WHERE id = ?;'''
    cursor = conn.cursor()
    cursor.execute(sql, (new_price, id,))
    conn.commit()


def delete_product(conn, id:int):
    sql = '''DELETE FROM products WHERE id = ?;'''
    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    conn.commit()


def select_all_product(conn):
    sql = '''SELECT * FROM products;'''
    cursor = conn.cursor()
    rows = cursor.execute(sql).fetchall()
    for row in rows:
        print(row)


def select_cheap(conn):
    sql = '''SELECT * FROM products WHERE price < 100 AND quantity > 5;'''
    cursor = conn.cursor()
    rows = cursor.execute(sql).fetchall()
    for row in rows:
        print(row)


def search_product(conn, keyword):
    cursor = conn.cursor()
    sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
    settings = ('%' + keyword + '%',)
    rows = cursor.execute(sql, settings).fetchall()
    
    print("Результаты поиска:")
    for row in rows:
        print(row)

connection = create_connection("produkt.db")
if connection:
    print("Database connected!")
    create_table(connection, sql_create_produkt_table)
    
    create_produkt(connection, ("помидор", 30.2, 50))
    create_produkt(connection, ("огурцы",  21.5, 40))
    create_produkt(connection, ("баклажан", 44.5 ,60 ))
    create_produkt(connection, ("тукум", 12.3, 50))
    create_produkt(connection, ("помидор",30.21, 50))
    create_produkt(connection, ("помидор",30.21, 50))
    create_produkt(connection, ("помидор",30.21, 50))
    create_produkt(connection, ("помидор",30.21, 50))
    create_produkt(connection, ("помидор",30.21, 50))
    create_produkt(connection, ("помидор", 30.21, 50))
    create_produkt(connection, ("помидор", 30.21, 50))
    create_produkt(connection, ("помидор", 30.21, 50))
    create_produkt(connection, ("помидор", 30.21, 50))
    create_produkt(connection, ("помидор", 30.21, 50))
    create_produkt(connection, ("помидор", 30.12, 40))


