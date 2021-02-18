import sqlite3
import time, random
from util.SQL import *
# Setup File
con=sqlite3.connect('./atomgreens.db')
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

    # Check that tables have been created
    cur.execute(SELECT_TBLE_NAMES)
    print(cur.fetchall())

def add_device(device, sensor=False):
    # Populate Sensor table
    cur.execute(DEV_INSRT, (device, sensor))

def add_node(piId, devId, active=True):
    cur.execute(NODE_INSRT, (piId, devId, active))

def add_meas(piId, devId, val):
    result = cur.execute(SELECT_NODEID, (piId, devId)).fetchone()
    if result:
        id = result[0]
        meas_data = (id, int(time.time()), val)
    else:
        add_device(piId, devId)
        meas_data = (cur.lastrowid, int(time.time()), val)

    print('Record to be inserted: ')
    print(meas_data)
    cur.execute(MEAS_INSRT, meas_data)


def view_create():
    #Create All current sensor information view
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
    GROUP BY measurements.nodeId"""
    print(cur.execute(STATUS_STATE_VIEW).fetchall())

    #Create Indepent Sensor View
    cur.execute(create_status_view("pi0_2_status", 2))
    print(cur.execute(select_table("pi0_2_status")).fetchall())

    # Pi4 Sensor View (for water status ect)
    cur.execute(create_status_view("pi4_status", 1))
    print('View test:')
    print(cur.execute(select_table("pi4_status")).fetchall())



if __name__ == "__main__":
    create_tables()
    add_device('humidity', True)
    add_device('temperature', True)
    add_device('weight', True)
    add_device('watering actuator')
    add_device('red light')
    add_device('blue light')
    add_device('air pump')
    add_device('water pump')
    add_device('ph pump')
    add_device('ec pump')
    add_device('ph', True)
    add_device('EC', True)
    add_device('water temperature', True)
    add_device('water level', True)
    add_device('heater')
    add_device('cooler')

    # Populate active_device tables
    for pi in range(1, 5):
        for dev in range(1,5):
            add_node(pi, dev)

    # Populate measurement table
    for rec in range(1,40):
        add_meas(random.randint(1,4), random.randint(1,4), random.randint(1,50))
    # Create Views
    view_create()
    con.commit()
