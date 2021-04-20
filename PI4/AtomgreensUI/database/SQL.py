DEV_INSRT = """INSERT INTO devices (device, sensor) VALUES (?, ?)"""
NODE_INSRT = """INSERT INTO nodes (piId, devId, active) VALUES (?,?,?)"""
MEAS_INSRT = """INSERT INTO measurements (nodeId, epoch_time, val)  VALUES (?,?,?)"""
RUN_START_WSTOP = """INSERT INTO runs (piId, start, stop)  VALUES (?,?,?)"""
RUN_START = """INSERT INTO runs (piId, start)  VALUES (?,?)"""

SELECT_NODEID = """SELECT id FROM nodes WHERE piId=? AND devId=?"""
SELECT_TBLE_NAMES = "SELECT name FROM sqlite_master WHERE type='table'"
SELECT_VIEW_NAMES = "SELECT name FROM sqlite_master WHERE type='view'"

EN_FK = "PRAGMA foreign_keys = 1"
DIS_FK = "PRAGMA foreign_keys = 0"

SELECT_PI_SENSOR_ALL = """SELECT devices.device AS device, measurements.val AS val, measurements.epoch_time AS etime 
                            FROM measurements
                            INNER JOIN active_nodes ON active_nodes.id = measurements.nodeId
                            INNER JOIN devices ON devices.id = active_nodes.devId
                            WHERE active_nodes.piId = ?; """

SELECT_PI_SENSOR_BETWEEN = """SELECT devices.device AS device, measurements.val AS val, measurements.epoch_time AS etime 
                            FROM measurements
                            INNER JOIN active_nodes ON active_nodes.id = measurements.nodeId
                            INNER JOIN devices ON devices.id = active_nodes.devId
                            WHERE active_nodes.piId = ? AND measurements.epoch_time BETWEEN ? and ?;"""

SELECT_EXPIRED_RUNS = """SELECT * 
                            FROM runs
                            WHERE stop < ? ;"""


PI4_STATUS = """SELECT device, val FROM pi4_status"""

STATUS = """SELECT device, val FROM status"""

SELECT_LATEST_PIDEV="""SELECT * FROM status WHERE devId=? and piId=?"""

ADD_CONDITION_DEFAULT="""INSERT INTO flags (flag) VALUES (?)"""
ADD_CONDITION="""INSERT INTO flags (flag, state) VALUES (?, ?)"""


def create_status_view(name, ID):
    return "CREATE VIEW " + name + " AS SELECT * FROM status WHERE piId=" + str(ID)

def select_table(tb_name):
    return "SELECT * FROM " + str(tb_name)
