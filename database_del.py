import sqlite3 as sl
con = sl.connect('deitabeiza.db')
if con:
    with con:
        del_query = con.execute("""SELECT name FROM sqlite_master  
      WHERE type='table'; """)
        del_query = [i[0] for i in del_query.fetchall() if i[0] != 'sqlite_sequence']
        print(del_query)
        if del_query:
            print('base is dead now')
            for i in del_query:
                con.execute(f"""
                        DROP TABLE IF EXISTS '{i}'
                    """)
        else:
            print('base is dead')