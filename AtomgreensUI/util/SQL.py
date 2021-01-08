DEV_INSRT = """INSERT INTO active_devices (piID, sensorId) VALUES (?, ?)"""
SENSOR_INSRT = """INSERT INTO sensors (sensor) VALUES (?)"""
MEAS_INSRT = """INSERT INTO measurements (devId, epoch_time, val)  VALUES (?,?,?)"""

SELECT_DEVID = """SELECT id FROM active_devices WHERE piID=? AND sensorId=?"""
SELECT_TBLE_NAMES = "SELECT name FROM sqlite_master WHERE type='table'"
SELECT_VIEW_NAMES = "SELECT name FROM sqlite_master WHERE type='view'"

EN_FK = "PRAGMA foreign_keys = 1"
DIS_FK = "PRAGMA foreign_keys = 0"

SELECT_PI_SENSOR_ALL = """SELECT sensors.sensor AS sensor, measurements.val AS val, measurements.epoch_time AS etime FROM measurements
                            INNER JOIN active_devices ON active_devices.id = measurements.devId
                            INNER JOIN sensors ON sensors.id = active_devices.sensorId
                            WHERE active_devices.piId = ?; """

SELECT_PI_SENSOR_BETWEEN = """SELECT sensors.sensor AS sensor, measurements.val AS val, measurements.epoch_time AS etime FROM measurements
                            INNER JOIN active_devices ON active_devices.id = measurements.devId
                            INNER JOIN sensors ON sensors.id = active_devices.sensorId
                            WHERE active_devices.piId = ? AND measurements.epoch_time BETWEEN ? and ?; """

PI4_STATUS = """SELECT sensor, val FROM pi4_status"""

def create_status_view(name, ID):
    return "CREATE VIEW " + name + " AS SELECT * FROM status WHERE piId=" + str(ID)

def select_table(tb_name):
    return "SELECT * FROM " + str(tb_name)