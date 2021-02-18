import sqlite3, time
from util.paths import db_dir
from util.SQL import SELECT_NODEID, MEAS_INSRT, NODE_INSRT

def connect(dp_path=db_dir):
    print(db_dir)
    return sqlite3.connect(dp_path)


def query(table, queryStr):
    conn = connect()
    cur = conn.cursor()
    cur.execute(queryStr)

def add_meas(piId, sensId, val, dbpath=db_dir):
    conn = connect(dbpath)
    cur = conn.cursor()
    result = cur.execute(SELECT_NODEID, (piId, sensId)).fetchone()
    if result:
        id = result[0]
        meas_data = (id, int(time.time()), val)
        print('Record to be inserted: ' + str(meas_data))
        cur.execute(MEAS_INSRT, meas_data)
    else:
        print('Invalid piID/DeviceID combination')
    conn.close()

def add_node(piId, devId, active=True, dbpath=db_dir):
    conn = connect(dbpath)
    cur = conn.cursor()
    cur.execute(NODE_INSRT, (piId, devId, active))
    conn.close()