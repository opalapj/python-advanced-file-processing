import sqlite3


con = sqlite3.connect('data/todo.db')
cur = con.cursor()

# Setting the priority to 20 for a task with id equal to 1.
cur.execute('UPDATE tasks SET priority = ? WHERE id = ?', (50, 1))
con.commit()
con.close()
