import sqlite3, time
from database.paths import db_dir
from database.SQL import SELECT_NODEID, MEAS_INSRT, NODE_INSRT, RUN_START_WSTOP
# Setup File
con=sqlite3.connect('./atomgreens.db')
cur = con.cursor()

def connect(dp_path=db_dir):
    return sqlite3.connect(dp_path)

def query(queryStr):
    conn = connect()
    cur = conn.cursor()
    return [item for item in cur.execute(queryStr)]    
    
def add_meas(piId, devId, val, dbpath=db_dir):
    conn = connect(dbpath)
    cur = conn.cursor()
    etime=int(time.time())
    result = cur.execute(SELECT_NODEID, (piId, devId)).fetchone()
    if result:
        id = result[0]
        meas_data = (id, etime, val)
    else:
        add_node(piId, devId)
        meas_data = (cur.lastrowid, etime, val)
    print('Record to be inserted: ')
    print(meas_data)
    cur.execute(MEAS_INSRT, meas_data)
    conn.commit()
    conn.close()
    

def add_node(piId, devId, active=True, dbpath=db_dir):
    conn = connect(dbpath)
    cur = conn.cursor()
    cur.execute(NODE_INSRT, (piId, devId, active))
    conn.close()
    
def new_run(piId, microgreen, runTime=604800, dbpath=db_dir):
    # Populate Sensor table
    t = int(time.time())
    conn = connect(dbpath)
    cur = conn.cursor()
    cur.execute(RUN_START_WSTOP, (piId, t, t + runTime, microgreen))
    conn.commit()
    conn.close()
