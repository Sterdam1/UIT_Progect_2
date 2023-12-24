import sqlite3 as sl

connect = sl.connect('deitabeiza.db')


# req file
class Double_Dragon:
    def __init__(self):
        global connect
        self.con = connect

    def get_good(self):
        rus = ['Название товара', 'Цена товара', 'Категория товара', 'Артикул', 'Масса товара',
               'Название файла характеристик', 'Название склада', 'Испорчен', 'Срок годности',
               'Количество доступно', 'Количество в ожидании']
        with self.con as con:
            goods = con.execute(""" select * from Goods """).fetchall()
            for i in range(len(goods)):
                goods[i] = goods[i][1:]
            return rus, goods

    def get_table_names(self) -> list:
        """
        gets all table names as strings.

        :return: table names
        :rtype: list
        """
        with self.con as con:
            names = con.execute("""SELECT name FROM sqlite_master  
          WHERE type='table'; """)
            names = [i[0] for i in names.fetchall() if i[0] != 'sqlite_sequence']
        return names

    def get_table_by_name(self, name: str) -> list:
        """
        gets all from a table.

        :param name: table name as string, as example 'Goods'
        :return: all table contains
        :rtype: list
        """
        with self.con as con:
            goods = con.execute(f""" select * from '{name}' """).fetchall()
        return goods




db = Double_Dragon()

# misc shit nothing to see here
"""
        Название
        товара                               good_name TEXT,
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
        
        Категория
        товара
        
        Артикул
        
        Срок
        годности
        
        Остаток
        
        Номер
        паспорта
        
        Масса
"""
