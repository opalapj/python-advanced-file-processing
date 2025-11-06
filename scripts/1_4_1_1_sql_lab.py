import sqlite3


class DBMS:

    def __init__(self):
        self.con = None
        self.cur = None
        print('Welcome to python/SQLite interface, enjoy!')

    def open_connection(self, db_name):
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()

    def close_connection(self):
        self.con.close()

    def fetch_db_content(self):
        res = self.cur.execute("SELECT name FROM sqlite_master")
        print(res.fetchall())

    def create_table(self, table_name):
        query = f'''CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
            );'''
        self.cur.execute(query)

    def fetch_table_content(self, table_name):
        query = f'SELECT * FROM {table_name}'
        results = self.cur.execute(query)
        self.printer(results)

    def delete_table_content(self, table_name):
        query = f'DELETE FROM {table_name}'
        self.cur.execute(query)
        self.con.commit()

    def insert_rows(self, table_name, rows):
        for row in rows:
            name, age = row[0], row[1]
            if self.name_check(name) & self.age_check(age):
                query = f'INSERT INTO {table_name} (name, age) VALUES (?, ?)'
                self.cur.execute(query, (name, age))
                self.con.commit()
            else:
                print('Row adding failed.')

    def fetch_rows(self, table_name, column_name, data):
        query = f'SELECT * FROM {table_name} WHERE {column_name} = ?'
        results = self.cur.execute(query, (data,))
        self.printer(results)

    def update_rows(
            self,
            table_name,
            column_name_from,
            data_from,
            column_name_to,
            data_to
    ):
        query = f'''UPDATE {table_name}
                SET {column_name_to} = ?
                WHERE {column_name_from} = ?'''
        self.cur.execute(query, (data_to, data_from))
        self.con.commit()

    def delete_rows(self, table_name, column_name, data):
        query = f'DELETE FROM {table_name} WHERE {column_name} = ?'
        self.cur.execute(query, (data,))
        self.con.commit()

    @staticmethod
    def age_check(age):
        if age < 18:
            print('The age cannot be less than 18!')
            return False
        else:
            return True

    @staticmethod
    def name_check(name):
        if name == '':
            print('The name cannot be an empty string!')
            return False
        else:
            return True

    @staticmethod
    def printer(results):
        desc = list(results.description)
        results = list(results)
        results.insert(0, tuple(map(lambda x: x[0], desc)))
        results.insert(1, (3*'-', 20*'-', 3*'-'))
        for row in results:
            print(f'{row[0]:<3} | {row[1]:20} | {row[2]}')


db = 'data/ner.db'
table = 'team'
members = [('Marcin', 40), ('Edward', 57), ('Artur', 44), ('Sebastian', 37)]
new_member_1 = [('Piotr', 28)]
new_member_2 = [('Young', 16)]
new_member_3 = [('', 100)]

dbms = DBMS()
dbms.open_connection(db)
dbms.fetch_db_content()

dbms.create_table(table)
dbms.fetch_db_content()
dbms.fetch_table_content(table)
dbms.delete_table_content(table)

dbms.insert_rows(table, members)
dbms.insert_rows(table, new_member_1)
dbms.insert_rows(table, new_member_2)
dbms.insert_rows(table, new_member_3)
dbms.fetch_rows(table, 'id', 2)
dbms.fetch_rows(table, 'name', 'Edward')
dbms.fetch_rows(table, 'age', 28)
dbms.update_rows(table, 'name', 'Edward', 'age', 50)
dbms.delete_rows(table, 'id', 5)
