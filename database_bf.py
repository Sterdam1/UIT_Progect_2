import sqlite3 as sl
con = sl.connect('deitabeiza.db')

# import sqlite3
# from sqlite3 import Error
#
# La-li-lu-le-lo
# def create_connection(db_file):
#     """ create a database connection to the SQLite database
#         specified by db_file
#     :param db_file: database file
#     :return: Connection object or None
#     """
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#         return conn
#     except Error as e:
#         print(e)
#
#     return conn
#
# def create_table(conn, create_table_sql):
#     """ create a table from the create_table_sql statement
#     :param conn: Connection object
#     :param create_table_sql: a CREATE TABLE statement
#     :return:
#     """
#     try:
#         c = conn.cursor()
#         c.execute(create_table_sql)
#     except Error as e:
#         print(e)

# run this file if u need to fill the base
# make sure that base is dead before in database_del.py file - run the file just for sure
if __name__ == '__main__':
    goodies_lists = [["Книга", 350.0, 1, 1234, 0.5, "Book_1.json", 1, 0, '2024-06-30', 50, 0],
                     ["Шоколад", 50.0, 2, 5678, 0.2, "Chocolate_1.json", 2, 0, '2024-12-31', 100, 0],
                     ["Монитор", 5000.0, 3, 9012, 3.0, "Display_1.json", 3, 0, '2024-01-31', 20, 0],
                     ["Кофеварка", 2000.0, 4, 3456, 1.5, "Coffee_maker_1.json", 4, 0, '2024-12-31', 10, 0],
                     ["Ноутбук", 40000.0, 5, 7890, 2.0, "Laptop_1.json", 5, 0, '2024-05-31', 5, 0],
                     ["Мяч для футбола", 1000.0, 6, 2345, 0.4, "Ball_1.json", 6, 0, '2023-08-31', 30, 0],
                     ["Наушники", 3000.0, 7, 6789, 0.2, "Headphones_1.json", 7, 0, '2023-04-30', 15, 0],
                     ["Ковер", 8000.0, 8, 1234, 5.0, "Carpet_1.json", 8, 0, '2025-12-31', 3, 0],
                     ["Футболка", 500.0, 9, 5678, 0.1, "T-shirt_1.json", 9, 0, '2024-10-31', 50, 0],
                     ["Кроссовки", 7000.0, 10, 9012, 0.8, "Sneakers_1.json", 10, 0, '2024-03-31', 10, 0],
                     ["Ручка", 20.0, 11, 3456, 0.01, "Pen_1.json", 11, 0, '2024-12-31', 200, 0],
                     ["Книжный шкаф", 15000.0, 12, 7890, 50.0, "Bookcase_1.json", 12, 0, '2026-06-30', 1, 0],
                     ["Телевизор", 25000.0, 3, 2345, 10.0, "TV_1.json", 3, 0, '2024-11-30', 5, 0],
                     ["Чайник", 1500.0, 4, 6789, 1.0, "Kettle_1.json", 4, 0, '2023-09-30', 7, 0],
                     ["Кошелек", 1000.0, 13, 1234, 0.1, "Wallet_1.json", 13, 0, '2022-12-31', 20, 0],
                     ["Смартфон", 20000.0, 5, 5678, 0.2, "Smartphone_1.json", 5, 0, '2024-08-31', 3, 0]]



    with con:
        # Goods
        con.execute("""
            CREATE TABLE IF NOT EXISTS Goods(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                good_name TEXT,
                price REAL,
                category_id,
                vendor_сode INTEGER,
                mass REAL,
                properties_json TEXT,
                depot_id,
                flag_expired INTEGER,
                expiration_date TEXT,
                amount,
                on_hold INTEGER
            )
        """)

        # Goods_list
        con.execute('''
                        CREATE TABLE IF NOT EXISTS Goods_list(
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        good_id INTEGER,
                        amount FLOAT,
                        list_id INTEGER)
                        ''')

        # Category
        con.execute('''
                        CREATE TABLE IF NOT EXISTS Category(
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        category_name TEXT)
                        ''')


        # Depots
        con.execute('''
                        CREATE TABLE IF NOT EXISTS Depots(
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        depot_name TEXT,
                        location_text TEXT,
                        location_gps TEXT)
                        ''')


        # Contractors
        con.execute('''
                        CREATE TABLE IF NOT EXISTS Contractors(
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        org_name TEXT,
                        phone INTEGER,
                        location TEXT,
                        unp TEXT,
                        depots_id INTEGER,
                        type TEXT)
                        ''')

        # Docs
        con.execute('''
                        CREATE TABLE IF NOT EXISTS Docs(
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        doc_type TEXT,
                        prefix TEXT,
                        number INTEGER,
                        sender TEXT,
                        receiver TEXT,
                        date TEXT,
                        driver TEXT,
                        pass_issued INTEGER,
                        pass_expired INTEGER,
                        proxy TEXT,
                        contract_num INTEGER,
                        list_id INTEGER)
                        ''')

        # Oder
        con.execute('''
                        CREATE TABLE IF NOT EXISTS Oder(
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        time_placed TEXT,
                        delivery_time TEXT,
                        state TEXT,
                        total_price FLOAT,
                        driver_id INTEGER,
                        location TEXT,
                        list_id INTEGER)
                        ''')


        sql_insert = '''INSERT OR IGNORE INTO Goods (good_name, price, category_id, vendor_сode, mass, properties_json, depot_id, flag_expired, expiration_date, amount, on_hold) VALUES (?,?,?,?,?,?,?,?,?,?,?)'''
        for i in goodies_lists:
            con.execute(sql_insert, i)
        else:
            print('database goodies ready for duty')


