import sqlite3


# Method .connect() creates new db or connects to existing db - return Connection object.
# Their main purpose is creating Cursor objects, and Transaction control.
con = sqlite3.connect("data/todo.db")

# The method .cursor() creates a Cursor object that allows any SQL statements to be executed in the database.
cur = con.cursor()

cur.execute("""CREATE TABLE tasks (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL
);""")

# Running the above program twice will throw an exception.
# Solution to omit error caused by existence of table.
cur.execute("""CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL
);""")
