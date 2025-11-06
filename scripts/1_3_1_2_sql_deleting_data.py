import sqlite3


con = sqlite3.connect('data/todo.db')
cur = con.cursor()

# Removing the task with id = 1.
cur.execute('''
DELETE FROM tasks
WHERE id = ?;
''', (1,))

# Removing all the tasks.
cur.execute('''
DELETE FROM tasks;
''')

con.commit()
con.close()

con = sqlite3.connect('data/todo.db')
cur = con.cursor()

# Removing table.
cur.execute('''
DROP TABLE IF EXISTS tasks;
''')
con.commit()
con.close()
