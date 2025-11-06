import logging

import sqlalchemy as sa


# Set constants.
DRIVERNAME = "sqlite+pysqlite"
DATABASE = "todo.db"

CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL
)
;
"""

INSERT_TASKS = """
INSERT INTO tasks (name, priority)
VALUES (:name, :priority)
;
"""

TASKS = [
    {"name": "My first task", "priority": 1},
    {"name": "My second task", "priority": 5},
    {"name": "My third task", "priority": 10},
]

# Enable logging.
logging.basicConfig()
logging.getLogger("sqlalchemy").setLevel(logging.INFO)

# Creating URLs programmatically.
url = sa.URL.create(
    drivername=DRIVERNAME,
    database=DATABASE,
)

# Establishing connectivity - the engine.
engine = sa.create_engine(
    url=url,
)

# Getting a connection using context manager.
with engine.connect() as conn:
    conn.execute(
        statement=sa.text(text=CREATE_TABLE),
    )
    conn.execute(
        statement=sa.text(text=INSERT_TASKS),
        parameters=TASKS,
    )
    conn.commit()
