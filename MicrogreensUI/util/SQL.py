DEV_INSRT = """INSERT INTO active_devices (piID, sensorId) VALUES (?, ?)"""
SENSOR_INSRT = """INSERT INTO sensors (sensor) VALUES (?)"""
MEAS_INSRT = """INSERT INTO measurements (devId, epoch_time, val)  VALUES (?,?,?)"""

SELECT_DEVID = """SELECT id FROM active_devices WHERE piID=? AND sensorId=?"""
SELECT_TBLE_NAMES = "SELECT name FROM sqlite_master WHERE type='table'"
SELECT_VIEW_NAMES = "SELECT name FROM sqlite_master WHERE type='view'"

EN_FK = "PRAGMA foreign_keys = 1"
DIS_FK = "PRAGMA foreign_keys = 0"

def create_status_view(name, ID):
    return "CREATE VIEW " + name + " AS SELECT * FROM status WHERE piId=" + str(ID)

def select_table(tb_name):
    return "SELECT * FROM " + str(tb_name)