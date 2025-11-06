import sqlite3


# Treating cursor object as an iterator.
con = sqlite3.connect('data/todo.db')
cur = con.cursor()
for id_, name, priority in cur.execute('SELECT * FROM tasks'):
    print(f'{id_:<3} | {name:20} | {priority}')
con.close()

# Using .fetchall() method.
con = sqlite3.connect('data/todo.db')
cur = con.cursor()
cur.execute('SELECT * FROM tasks')
rows = cur.fetchall()
for id_, name, priority in rows:
    print(f'{id_:<3} | {name:20} | {priority}')
con.close()

# Using .fetchone() method to retrieve the next available record.
con = sqlite3.connect('data/todo.db')
cur = con.cursor()
cur.execute('SELECT * FROM tasks')
row = cur.fetchone()
print(row)
row = cur.fetchone()
print(row)
con.close()
