import sqlite3, time
from database.paths import db_dir
from database.SQL import *


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

def get_latest(pi, devId, dbpath=db_dir):
    conn = connect(dbpath)
    cur = conn.cursor()
    data = list(cur.execute(SELECT_LATEST_PIDEV, (pi, devId)).fetchall())
    conn.close()
    return data

def new_run(piId, runTime=604800, dbpath=None):
    conn = connect(dbpath)
    cur = conn.cursor()
    cur.execute(RUN_START_WSTOP, (piId, time.time(), time.time()+runTime))
    conn.commit()
    conn.close()