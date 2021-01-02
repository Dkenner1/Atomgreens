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

    CREATE_SENSOR_TABLE = """ CREATE TABLE IF NOT EXISTS sensors (id INTEGER PRIMARY KEY, sensor TEXT NOT NULL)"""
    cur.execute(CREATE_SENSOR_TABLE)
    CREATE_DEVS_TBL_SQL = """ CREATE TABLE IF NOT EXISTS active_devices (id INTEGER PRIMARY KEY, piID INTEGER, sensorId INTEGER, FOREIGN KEY (sensorId) REFERENCES sensors (id))"""
    cur.execute(CREATE_DEVS_TBL_SQL)
    CREATE_MEAS_TABLE_SQL = """ CREATE TABLE IF NOT EXISTS measurements (id INTEGER PRIMARY KEY, devId INTEGER NOT NULL CHECK (typeof(devId) = 'integer'), epoch_time INTEGER NOT NULL CHECK (typeof(epoch_time) = 'integer'), val REAL NOT NULL, FOREIGN KEY (devId) REFERENCES active_devices (id))"""
    cur.execute(CREATE_MEAS_TABLE_SQL)

    # Check that tables have been created
    cur.execute(SELECT_TBLE_NAMES)
    print(cur.fetchall())

def add_sensor(sensType):
    # Populate Sensor table
    cur.execute(SENSOR_INSRT, (sensType,))

def add_device(piId, sensId):
    cur.execute(DEV_INSRT, (pi, sen))

def add_meas(piId, sensId, val):
    result = cur.execute(SELECT_DEVID, (piId, sensId)).fetchone()
    if result:
        id = result[0]
        meas_data = (id, int(time.time()), val)
    else:
        add_device(piId, sensId)
        meas_data = (cur.lastrowid, int(time.time()), val)

    print('Record to be inserted: ')
    print(meas_data)
    cur.execute(MEAS_INSRT, meas_data)


def view_create():
    #Create All current sensor information view
    SENSOR_STATE_VIEW = """CREATE VIEW status AS 
    SELECT measurements.devId as devId, active_devices.piId AS piID, active_devices.sensorId AS sensorId, sensors.sensor AS sensor, measurements.val AS val, MAX(measurements.epoch_time) AS 'epoch_time' 
    FROM measurements 
    INNER JOIN active_devices ON measurements.devId = active_devices.id 
    INNER JOIN sensors ON active_devices.sensorId = sensors.id 
    GROUP BY measurements.devId"""
    print(cur.execute(SENSOR_STATE_VIEW).fetchall())

    #Create Indepent Sensor View
    cur.execute(create_status_view("pi0_2_status", 2))
    print(cur.execute(select_table("pi0_2_status")).fetchall())

    # Pi4 Sensor View (for water status ect)
    cur.execute(create_status_view("pi4_status", 1))
    print('View test:')
    print(cur.execute(select_table("pi4_status")).fetchall())



if __name__ == "__main__":
    create_tables()
    add_sensor('weight')
    add_sensor('temperature')
    add_sensor('humidity')
    add_sensor('water level')
    # Populate active_device tables
    for pi in range(1, 5):
        for sen in range(1,5):
            add_device(pi,sen)

    # Populate measurement table
    for rec in range(1,40):
        add_meas(random.randint(1,4), random.randint(1,4), random.randint(1,50))
    # Create Views
    view_create()
    con.commit()
