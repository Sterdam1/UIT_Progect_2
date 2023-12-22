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
    goodies_list = [["Книга", 350.0, 1, 1234, 0.5, "Book_1.json", 1, 0, '2024-06-30', 50, 20],
                     ["Шоколад", 50.0, 2, 5678, 0.2, "Chocolate_1.json", 2, 0, '2024-12-31', 100, 0],
                     ["Монитор", 5000.0, 3, 9012, 3.0, "Display_1.json", 3, 0, '2024-01-31', 20, 10],
                     ["Кофеварка", 2000.0, 4, 3456, 1.5, "Coffee_maker_1.json", 1, 0, '2024-12-31', 10, 0],
                     ["Ноутбук", 40000.0, 5, 7890, 2.0, "Laptop_1.json", 2, 0, '2024-05-31', 5, 2],
                     ["Мяч для футбола", 1000.0, 6, 2345, 0.4, "Ball_1.json", 3, 0, '2023-08-31', 30, 0],
                     ["Наушники", 3000.0, 7, 6789, 0.2, "Headphones_1.json", 3, 0, '2023-04-30', 15, 0],
                     ["Ковер", 8000.0, 8, 1234, 5.0, "Carpet_1.json", 3, 0, '2025-12-31', 3, 2],
                     ["Футболка", 500.0, 9, 5678, 0.1, "T-shirt_1.json", 2, 0, '2024-10-31', 50, 0],
                     ["Кроссовки", 7000.0, 10, 9012, 0.8, "Sneakers_1.json", 1, 0, '2024-03-31', 10, 8],
                     ["Ручка", 20.0, 11, 3456, 0.01, "Pen_1.json", 1, 0, '2024-12-31', 200, 0],
                     ["Книжный шкаф", 15000.0, 12, 7890, 50.0, "Bookcase_1.json", 2, 0, '2026-06-30', 1, 1],
                     ["Телевизор", 25000.0, 3, 2345, 10.0, "TV_1.json", 3, 0, '2024-11-30', 5, 0],
                     ["Чайник", 1500.0, 4, 6789, 1.0, "Kettle_1.json", 3, 0, '2023-09-30', 7, 6],
                     ["Кошелек", 1000.0, 13, 1234, 0.1, "Wallet_1.json", 1, 0, '2022-12-31', 20, 0],
                     ["Смартфон", 20000.0, 5, 5678, 0.2, "Smartphone_1.json", 2, 0, '2024-08-31', 300, 9]]

    categories_list = [(1, "Книги"),
                        (2, "Сладости"),
                        (3, "Электроника"),
                        (4, "Бытовая техника"),
                        (5, "Смартфоны и гаджеты"),
                        (6, "Игры и игрушки"),
                        (7, "Наушники и акустика"),
                        (8, "Текстиль и ковры"),
                        (9, "Одежда"),
                        (10, "Обувь"),
                        (11, "Канцелярия"),
                        (12, "Мебель"),
                        (13, "Аксессуары")]
    depots_list = [("Склад 1", "Москва, ул. Тверская, д.1", "55.758460, 37.601079"),
                    ("Склад 2", "Санкт-Петербург, наб. реки Мойки, д.22", "59.935055, 30.325811"),
                    ("Склад 3", "Екатеринбург, ул. Ленина, д.45", "56.838011, 60.597465")]
    contractors_list = [("Иванов Иван", "ООО Рога и Копыта", 79123456789, "Москва, ул. Ленина, д.10", "123456789", 1, "Поставщик"),
                        ("Петров Петр", "ИП Петров", 79234567890, "Санкт-Петербург, пр. Невский, д.20", "234567890", 2, "Покупатель"),
                        ("Сидоров Сидор", "ООО Сидор и Ко", 79345678901, "Екатеринбург, ул. Кирова, д.5", "345678901", 3, "Поставщик"),
                        ("Козлов Константин", "ИП Козлов", 79456789012, "Москва, ул. Арбат, д.15", "456789012", 1, "Покупатель"),
                        ("Николаев Николай", "ОАО Николаев и партнеры", 79567890123, "Санкт-Петербург, ул. Рубинштейна, д.8", "567890123", 2, "Поставщик"),
                        ("Григорьев Григорий", "ИП Григорьев", 79678901234, "Екатеринбург, ул. Малышева, д.50", "678901234", 3, "Покупатель")]
    listy_of_goodylist = [(1, 20, 1),
                            (3, 10, 3),
                            (5, 2, 2),
                            (8, 2, 3),
                            (10, 8, 1),
                            (12, 1, 2),
                            (14, 6, 3),
                            (16, 9, 2)]
    oder_list = [('2023-12-22 12:00:00', '2023-12-24 15:00:00', 'in transit', 63000.00, 4, "Санкт-Петербург, наб. реки Мойки, д.22", 1)]
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
                        id INTEGER,
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
                        name,
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
        for i in goodies_list:
            con.execute(sql_insert, i)
        else:
            print('table Goods ready for duty')

        sql_insert = '''INSERT OR IGNORE INTO Category (id, category_name) VALUES (?,?)'''
        for i in categories_list:
            con.execute(sql_insert, i)
        else:
            print('table Category ready for duty')

        sql_insert = '''INSERT OR IGNORE INTO Depots (depot_name, location_text, location_gps) VALUES (?,?,?)'''
        for i in depots_list:
            con.execute(sql_insert, i)
        else:
            print('table Depots ready for duty')

        sql_insert = '''INSERT OR IGNORE INTO Contractors (name, org_name, phone, location, unp, depots_id, type) VALUES (?,?,?,?,?,?,?)'''
        for i in contractors_list:
            con.execute(sql_insert, i)
        else:
            print('table Contractors ready for duty')

        sql_insert = '''INSERT OR IGNORE INTO Goods_list (good_id, amount, list_id) VALUES (?,?,?)'''
        for i in listy_of_goodylist:
            con.execute(sql_insert, i)
        else:
            print('table Goods_list ready for duty')

        sql_insert = '''INSERT OR IGNORE INTO Oder (time_placed, delivery_time, state, total_price, driver_id, location, list_id) VALUES (?,?,?,?,?,?,?)'''
        for i in oder_list:
            con.execute(sql_insert, i)
        else:
            print('table Oder ready for duty')