import sqlite3
import time, random
from paths import db_dir
from SQL import *
from db import connect
# Setup File
con = sqlite3.connect('./atomgreens.db')
cur = con.cursor()


def create_tables():
    # Clear all previous tables/views to prevent repeat entries
    con.execute(DIS_FK)
    print('Current tables:')
    # Drop tables
    result = cur.execute(SELECT_TBLE_NAMES)
    result = result.fetchall()
    print(result)
    for item in result:
        cur.execute("DROP TABLE " + item[0])
    # Drop views
    result = cur.execute(SELECT_VIEW_NAMES)
    result = result.fetchall()
    print(result)
    for item in result:
        cur.execute("DROP VIEW " + item[0])

    # Check results
    print('Altered tables:')
    print(cur.execute(SELECT_TBLE_NAMES).fetchall())
    print(cur.execute(SELECT_VIEW_NAMES).fetchall())

    # Recreate Tables
    print('Table creation')
    con.execute(EN_FK)

    CREATE_DEV_TABLE = """CREATE TABLE IF NOT EXISTS devices 
    (id INTEGER PRIMARY KEY, 
    device TEXT UNIQUE NOT NULL, 
    sensor INTEGER DEFAULT 1 NOT NULL CHECK (sensor < 2) )"""
    cur.execute(CREATE_DEV_TABLE)

    CREATE_NODES_TBL_SQL = """CREATE TABLE IF NOT EXISTS nodes 
    (id INTEGER PRIMARY KEY, 
    piId INTEGER, 
    devId INTEGER,
    active INTEGER NOT NULL CHECK (active < 2),
    FOREIGN KEY (devId) REFERENCES devices (id)) """
    cur.execute(CREATE_NODES_TBL_SQL)

    CREATE_MEAS_TABLE_SQL = """ CREATE TABLE IF NOT EXISTS measurements 
    (id INTEGER PRIMARY KEY, 
    nodeId INTEGER NOT NULL, 
    epoch_time INTEGER NOT NULL CHECK (typeof(epoch_time) = 'integer'), 
    val REAL NOT NULL, 
    FOREIGN KEY (nodeId) REFERENCES nodes (id))"""
    cur.execute(CREATE_MEAS_TABLE_SQL)

    CREATE_RUNS_TABLE_SQL = """ CREATE TABLE IF NOT EXISTS runs 
    (id INTEGER PRIMARY KEY, 
    piId INTEGER NOT NULL, 
    start INTEGER NOT NULL, 
    stop INTEGER DEFAULT 0)"""
    cur.execute(CREATE_RUNS_TABLE_SQL)

    CREATE_FLAGS_TABLE_SQL = """ CREATE TABLE IF NOT EXISTS flags 
    (id INTEGER PRIMARY KEY, 
    flag INTEGER NOT NULL, 
    state INTEGER DEFAULT 0)"""
    cur.execute(CREATE_FLAGS_TABLE_SQL)

    # Check that tables have been created
    cur.execute(SELECT_TBLE_NAMES)
    print(cur.fetchall())


def start_run(piId, start=0, stop=0):
    # Populate Sensor table
    if stop != 0:
        cur.execute(RUN_START_WSTOP, (piId, start, stop))
    else:
        cur.execute(RUN_START, (piId, int(time.time())))


def add_device(device, sensor=False):
    # Populate Sensor table
    cur.execute(DEV_INSRT, (device, sensor))

def add_condition(flag, state=0):
    cur.execute(ADD_CONDITION, (flag, state))

def add_node(piId, devId, active=True):
    cur.execute(NODE_INSRT, (piId, devId, active))


def add_meas(piId, devId, val, etime=int(time.time()), dbpath=db_dir):
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


def view_create():
    # Create All current sensor information view
    ACTIVE_DEVS_VIEW = """CREATE VIEW active_nodes AS 
    SELECT * 
    FROM nodes
    WHERE active = 1"""
    print(cur.execute(ACTIVE_DEVS_VIEW).fetchall())
    STATUS_STATE_VIEW = """CREATE VIEW status AS 
    SELECT measurements.nodeId as nodeId, nodes.piId AS piID, nodes.devId AS devId, devices.device AS device, 
    measurements.val AS val, MAX(measurements.epoch_time) AS 'epoch_time' 
    FROM measurements 
    INNER JOIN nodes ON measurements.nodeId = nodes.id 
    INNER JOIN devices ON nodes.devId = devices.id
    WHERE devices.sensor=1
    GROUP BY measurements.nodeId"""
    print(cur.execute(STATUS_STATE_VIEW).fetchall())

    # Create Indepent Sensor View
    cur.execute(create_status_view("pi0_2_status", 2))
    print(cur.execute(select_table("pi0_2_status")).fetchall())

    # Pi4 Sensor View (for water status ect)
    cur.execute(create_status_view("pi4_status", 1))
    print('View test:')
    print(cur.execute(select_table("pi4_status")).fetchall())

    # Current runs
    CURRENT_RUNS_STATE_VIEW = """CREATE VIEW current_runs AS 
    SELECT *, MAX(start)
    FROM runs 
    GROUP BY piId"""
    print(cur.execute(CURRENT_RUNS_STATE_VIEW))


if __name__ == "__main__":
    create_tables()
    add_device('humidity', True)
    add_device('internal temperature', True)
    add_device('weight', True)
    add_device('watering actuator')
    add_device('red light')
    add_device('blue light')
    add_device('air pump')
    add_device('water pump')
    add_device('ph pump', True)
    add_device('ec pump', True)
    add_device('ph', True)
    add_device('EC', True)
    add_device('water temperature', True)
    add_device('water level', True)
    add_device('heater')
    add_device('cooler')
    add_device('external temperature', True)

    add_condition("MAINT")

    day = 86400
    hour = 3600
    eTime = time.time()

    start_run(1)
    start_run(2)
    start_run(3)
    start_run(4)
    start_run(5)
    start_run(5, int(eTime-7*day), int(eTime))
    # Populate active_device tables
    for pi in range(0, 5):
        for dev in range(1, 15):
            add_node(pi, dev)
            add_meas(pi, dev, 0)

    # Create Views
    view_create()
    con.commit()
