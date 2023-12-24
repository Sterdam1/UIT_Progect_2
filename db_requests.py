import sqlite3 as sl

connect = sl.connect('deitabeiza.db')


# req file
class DoubleDragon:
    table_names_dicty = {
        'Category': 'Категория',
        'Goods': 'Товары',
        'Depots': 'Склады',
        'Goods_list': 'Список товаров',
        'Bridge': 'Мост',
        'Oder': 'Заказ',
        'Docs': 'Документы',
        'Contractors': 'Контрагенты'
    }
    dicty_to_rus = {
        'cat_id': 'идентификатор категории',
        'dep_id': 'идентификатор склада',
        'br_id': 'идентификатор моста',
        'od_id': 'идентификатор заказа',
        'con_id': 'идентификатор контрагента',
        'docs_id': 'идентификатор документа',
        'list_id': 'идентификатор списка товаров',
        'category_id': 'идентификатор категории',
        'vendor_сode': 'артикул',
        'mass': 'масса',
        'properties_json': 'свойства в формате JSON',
        'depot_id': 'идентификатор склада',
        'flag_expired': 'флаг просроченности',
        'expiration_date': 'дата истечения срока годности',
        'on_hold': 'на удержании',
        'id': "идентификатор",
        'price': 'цена товара',
        'good_name': 'название товара',
        'good_id': 'идентификатор товара',
        'amount': 'количество',
        'group_id': 'идентификатор группы',
        'category_name': 'название категории',
        'depot_name': 'название склада',
        'location_text': 'адрес',
        'location_gps': 'координаты GPS',
        'order_id': 'идентификатор заказа',
        'doc_id': 'идентификатор документа',
        'name': 'имя',
        'org_name': 'название организации',
        'phone': 'телефон',
        'location': 'местоположение',
        'unp': 'УНП',
        'type': 'тип',
        'doc_type': 'тип документа',
        'prefix': 'префикс',
        'number': 'номер',
        'sender': 'отправитель',
        'receiver': 'получатель',
        'date': 'дата',
        'driver': 'водитель',
        'pass_issued': 'дата выдачи паспорта',
        'pass_expired': 'дата истечения срока действия паспорта',
        'proxy': 'доверенность',
        'contract_num': 'номер контракта',
        'time_placed': 'время размещения заказа',
        'delivery_time': 'время доставки',
        'state': 'состояние',
        'total_price': 'общая стоимость',
        'driver_id': 'идентификатор водителя'}

    def __init__(self):
        global connect
        self.con = connect

    def get_rus_columns(self, name: str) -> list:
        """
        gets all column names in table in russian.
        :param name: table name as string, as example 'Goods'
        """
        rus_listy = []
        with self.con as con:
            result = con.execute(f'''select * from pragma_table_info('{name}')''').fetchall()
            listy = [i[1] for i in result]
            for i in listy:
                rus_listy.append(DoubleDragon.dicty_to_rus[i])
        return rus_listy

    def get_table_names(self) -> list:
        """
        gets all table names as strings. except temporal ones.

        :return: table names
        :rtype: list
        """
        with self.con as con:
            names = con.execute("""SELECT name FROM sqlite_master  
          WHERE type='table'; """)
        return [i[0] for i in names.fetchall() if i[0] != 'sqlite_sequence']

    def get_table_by_name(self, name: str, with_id=False) -> list:
        """
        gets all from a table.

        :param name: table name as string, as example 'Goods'
        :param with_id: True if id is needed
        :return: all table contains
        :rtype: list
        """
        with self.con as con:
            if with_id:
                return con.execute(f""" select * from '{name}' """).fetchall()
            table_content = con.execute(f""" select * from '{name}' """).fetchall()
            return [table_content[i][1:] for i in range(len(table_content))]

    def get_items(self, table_name: str, values, by: str) -> list:
        """
        returns list of items searched by value (string or tuple). includes all matches i.e. 'in' not '=' in sqlite

        :param table_name: table name as string, as example 'Goods'
        :param values: tuple (if tuple - at least 2 items) i.e. ('Шоколад','Книга') or string of text i.e. 'Шоколад'
        :param by: string of text by which you filter table content, as example 'id'
        :return: list of matches
        :rtype: list
        """
        with self.con as con:
            if type(values) == str:
                values = "'" + values + "'"
                return con.execute(f""" select * from '{table_name}' where {by} in ({values}) """).fetchall()
            return con.execute(f""" select * from '{table_name}' where {by} in {values} """).fetchall()

    def get_fancy_goods(self, with_id=False) -> list:
        """
        gets all from a Goods table for end user without other tables ids.

        :param with_id: True if id is needed
        :return: table contains
        :rtype: list
        """
        with self.con as con:
            req = con.execute(f""" select id, good_name, price, category_name, vendor_сode, mass, properties_json, 
                depot_name, flag_expired, expiration_date, amount, on_hold, doc_id from Goods 
                INNER JOIN Category ON Goods.category_id = Category.cat_id 
                INNER JOIN Depots ON Goods.depot_id = Depots.dep_id """).fetchall()
            if with_id:
                return req
            return [req[i][1:] for i in range(len(req))]

    def del_table_content_by_ids(self, name: str, ids: list):
        """
        delete strings from any table. required name of table and list of ids

        :param name: table name as string, as example 'Goods'
        :param ids: list of id, as example [1, 2, 3] or [4]
        """
        print(f'''DELETE FROM '{name}'
                            WHERE id in {ids}''')
        with self.con as con:
            if len(ids) > 1:
                ids = tuple(ids)
                con.execute(f'''DELETE FROM '{name}' WHERE id in {ids}''')
            else:
                ids = ids[0]
                con.execute(f'''DELETE FROM '{name}' WHERE id in ({ids})''')

    def insert(self, name: str, values: tuple):
        """
        insert values into table. required name of table and tuple of values. id is not required

        :param name: table name as string, as example 'Goods'
        :param values: tuple of values i.e. ('Книга', 350.0, 1, 1234, 0.5, 'Book_1.json', 1, 0, '2024-06-30', 50, 20, 0))
        """
        with self.con as con:
            result = con.execute(f'''select * from pragma_table_info('{name}')''').fetchall()
            listy = tuple([i[1] for i in result if i[1] != 'id'])
            con.execute(f'''insert into '{name}' {listy} values {values}''')

    def insert_docs(self, doc_type=None, prefix=None, number=None, sender=None, receiver=None,
                    date=None, driver=None, pass_issued=None, pass_expired=None, proxy=None, contract_num=None):
        """
        pretty much work in progress
        maybe good enough?
        all of the parameters in oder of appearance in DB
        """
        with self.con as con:
            con.execute(f'''insert into Docs (doc_type, prefix, number, sender, receiver, 
            date, driver, pass_issued, pass_expired, proxy, contract_num) values {doc_type, prefix, number, sender,
                                                                                  receiver, date, driver, pass_issued, pass_expired, proxy, contract_num} ''')

    # the same as it ever was
    def update_cell(self, table: str, id: int, param: str, value: any):
        """
        Sets parameter(param) of item(by id) in table(table) to (value)
        """
        if type(value) == str:
            value = "'" + value + "'"
        with self.con as con:
            con.execute(f'''UPDATE {table}
                            SET '{param}' = {value}
                            WHERE id = {id} ''')


db = DoubleDragon()

# misc shit nothing to see here
"""
        select * from pragma_table_info('tblName')
"""
