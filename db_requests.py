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
        'client_id': 'идентификатор клиента',
        'dep_id': 'идентификатор склада',
        'br_id': 'идентификатор моста',
        'od_id': 'идентификатор заказа',
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

    def get_columns(self,
                    name: str):  # Написал Костя, в теории надо такая же фукнция только как fancy_columns или что-то типа того(Посвещается Андрею)
        """
        get all column names
        :param name: table name as string, as example 'Goods'
        """
        with self.con as con:
            result = con.execute(f'''select * from pragma_table_info('{name}')''').fetchall()
            return [i[1] for i in result]

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
                return con.execute(f""" select * from '{table_name}' where {by} LIKE {values} """).fetchall()
            return con.execute(f""" select * from '{table_name}' where {by} in {values} """).fetchall()

    def get_fancy_goods(self, with_id=False) -> list:
        """
        gets all from a Goods table for end user without other tables ids.

        :param with_id: True if id is needed
        :return: table contains
        :rtype: list
        """
        with self.con as con:
            req = con.execute(f""" select Goods.id, good_name, price, category_name, vendor_сode, mass, properties_json, 
                depot_name, flag_expired, expiration_date, amount, on_hold, doc_id from Goods 
                INNER JOIN Category ON Goods.category_id = Category.id 
                INNER JOIN Depots ON Goods.depot_id = Depots.id """).fetchall()
            if with_id:
                return req
            return [req[i][1:] for i in range(len(req))]

    def del_table_content_by_ids(self, name: str, ids: list):
        """
        delete strings from any table. required name of table and list of ids

        :param name: table name as string, as example 'Goods'
        :param ids: list of id, as example [1, 2, 3] or [4]
        :param id_name: name of the id column in table
        """
        with self.con as con:
            if len(ids) > 1:
                ids = tuple(ids)
                con.execute(f'''DELETE FROM '{name}' WHERE id in {ids}''')
            else:
                ids = ids[0]
                con.execute(f'''DELETE FROM '{name}' WHERE id in ({ids})''')

    def del_table_content_by_ids_concat(self, name: str, ids: list) -> str:
        """
        return string of text with delete statement. required name of table and list of ids

        :param name: table name as string, as example 'Goods'
        :param ids: list of id, as example [1, 2, 3] or [4]
        """
        if len(ids) > 1:
            ids = tuple(ids)
            return f''' DELETE FROM '{name}' WHERE id in {ids}; '''
        else:
            ids = ids[0]
            return f''' DELETE FROM '{name}' WHERE id in ({ids}); '''

    def insert(self, name: str, values: tuple) -> int:
        """
        insert values into table. required name of table and tuple of values. id is not required
        return that last id
        :param name: table name as string, as example 'Goods'
        :param values: tuple of values i.e. ('Книга', 350.0, 1, 1234, 0.5, 'Book_1.json', 1, 0, '2024-06-30', 50, 20, 0))
        """
        with self.con as con:
            result = con.execute(f'''select * from pragma_table_info('{name}')''').fetchall()
            listy = tuple([i[1] for i in result if i[1] != 'id'])
            con.execute(f'''insert into '{name}' {listy} values {values}''')
        return con.execute(f'''select max(id) from '{name}' ''').fetchall()[0][0]

    def insert_concat(self, name: str, values: tuple) -> str:
        """
        return string with insert values into table statement. required name of table and tuple of values.
        id is not required

        :param name: table name as string, as example 'Goods'
        :param values: tuple of values i.e. ('Книга', 350.0, 1, 1234, 0.5, 'Book_1.json', 1, 0, '2024-06-30', 50, 20, 0))
        """
        with self.con as con:
            result = con.execute(f'''select * from pragma_table_info('{name}')''').fetchall()
            listy = tuple([i[1] for i in result if i[1] != 'id'])
            return f''' insert into '{name}' {listy} values {values}; '''

    def insert_docs(self, number, doc_type='', prefix='', sender='', receiver='',
                    date='', driver='', pass_issued='', pass_expired='', proxy='', contract_num=''):
        """
        number required for requests to work, so it's mandatory
        everything else can be empty string for now
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

    def doc_index_increment(self, doc_type):
        """
        Increment number for doctype, note that breaks if any numbers are empty strings
        """
        with self.con as con:
            num = con.execute(f'''select max(number) + 1 FROM Docs WHERE doc_type = '{doc_type}' ''').fetchall()[0][0]
            if not num:
                return 1
            return num

    def goods_on_pause(self, bridge_id, return_goods=False):
        """
        Withdraws of adds back goods for certain bridge_id batch of goods_list
        """
        goods_list = [(i[1], i[2]) for i in self.get_items('Goods_list', str(bridge_id), 'group_id')]
        with self.con as con:
            for good_id, amount in goods_list:
                if not return_goods:
                    con.execute(
                        f''' update Goods set amount = amount - {amount}, on_hold = on_hold + {amount} WHERE id = '{good_id}' ''')
                else:
                    con.execute(
                        f''' update Goods set amount = amount + {amount}, on_hold = on_hold - {amount} WHERE id = '{good_id}' ''')

    def create_oder(self, time_placed, driver_id, client_id, location, order_list, delivery_time='1 hour', state=1,
                    doc_id=''):
        """
        creates oder with set parameters and adds bridge and goods_list counterparts
        order list in [(good_id, amount), ...] like
        """
        prices = [i[2] for i in self.get_items('Goods', tuple([i[0] for i in order_list]), 'id')]
        total_price = sum([order_list[i][1] * prices[i] for i in range(len(order_list))])
        last_id = self.insert('Oder', (time_placed, delivery_time,
                                      state, total_price, driver_id, location, client_id))
        bridge_id = self.insert('Bridge', (last_id, doc_id))
        for good_id, amount in order_list:
            self.insert('Goods_list', (good_id, amount, bridge_id))
        self.goods_on_pause(bridge_id)

    def goods_termination(self, bridge_id):
        """
        Terminates goods from on_hold when they already shipped - i.e. final shipment of goods
        """
        goods_list = [(i[1], i[2]) for i in DoubleDragon.get_items(self, 'Goods_list', str(bridge_id), 'group_id')]
        with self.con as con:
            for good_id, amount in goods_list:
                con.execute(
                    f''' update Goods set on_hold = on_hold - {amount} WHERE id = '{good_id}' ''')

db = DoubleDragon()

# misc shit nothing to see here
"""
        select * from pragma_table_info('tblName')
"""
