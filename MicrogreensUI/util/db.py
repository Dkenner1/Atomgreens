import sqlite3
from util.paths import db_dir

def connect(dp_path=db_dir):
    return sqlite3.connect(dp_path)


def query(table, queryStr):
    conn = connect()
    cur = conn.cursor()
    cur.execute(queryStr)