import sqlite3
from sqlite3 import Error

def get_all_employees():
    database = "./employees.db"
    conn = create_connection(database)
    conn.row_factory = sqlite3.Row
    with conn:
    
        cur = conn.cursor()
        cur.execute("SELECT gender, id FROM employees")
        rows = cur.fetchall()

        return [dict(ix) for ix in rows]


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn