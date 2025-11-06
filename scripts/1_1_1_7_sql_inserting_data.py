import sqlite3


con = sqlite3.connect('data/todo.db')
cur = con.cursor()

# Parameters (second parameter of .execute() method) - python values to bind
# to placeholders in sql. A dict if named placeholders are used.
# A sequence if unnamed placeholders are used. See How to use placeholders
# to bind values in SQL queries.
cur.execute('''
INSERT INTO tasks (name, priority)
VALUES (?, ?);
''', ('My first task', 1))  # This is the qmark style, sequence.

cur.execute('''
INSERT INTO tasks (name, priority)
VALUES (:task, :prior);
''', {'task': 'My second task', 'prior': 2})  # This is the named style, dictionary.

# The INSERT statement implicitly opens a transaction, which needs to be
# committed before changes are saved in the database (see Transaction control
# for details).
# Call con.commit() on the connection object to commit the transaction.
con.commit()
con.close()

con = sqlite3.connect('todo.db')
cur = con.cursor()
# For every item in parameters, repeatedly execute the parameterized SQL statement.
tasks = [
    ('My first task', 1),
    ('My second task', 5),
    ('My third task', 10),
]
cur.executemany('''
INSERT INTO tasks (name, priority)
VALUES (?, ?)
''', tasks)
con.commit()
con.close()
