from flask import Blueprint, render_template, json, \
    redirect, request, url_for
from database.db import connect
from database.SQL import *
from devices.trayCtrl import *
import time



main = Blueprint('main', __name__, template_folder='templates')


@main.route('/', methods=['GET', 'POST'])
def index():
    conn = connect()
    cur = conn.cursor()
    try:
        data = {item[0].replace(' ', '_'): item[1] for item in cur.execute(PI4_STATUS)}
    except:
        print("No pi4 table")
    eTime = time.time()
    startTimes = [None, None, None, None, None]
    for item in cur.execute("""SELECT piId, start, stop FROM current_runs""").fetchall():
        startTimes[item[0]-1] = round(100 * (eTime - item[1]) / (item[2]-item[1]+1), 1)

    weights = {item[0]: item[2] for item in
               cur.execute("""SELECT piID, device, val FROM status WHERE device='weight'""")}
    temps = {item[0]: item[2] for item in
               cur.execute("""SELECT piID, device, val FROM status WHERE device='internal temperature'""")}
    hums = {item[0]: item[2] for item in
             cur.execute("""SELECT piID, device, val FROM status WHERE device='humidity'""")}
    microgreens = {item[0]: item[1] for item in
                   cur.execute("""SELECT piID, type FROM current_runs""")}
    conn.close()
    print(microgreens)
    return render_template('index.html', status=data, times=startTimes, weights=weights, temps=temps, hums=hums, greenType=microgreens)


@main.route('/trayinfo/<trayid>', methods=['GET', 'POST'])
def data(trayid):
    conn = connect()
    cur = conn.cursor()
    eTime = time.time()
    time_range = eTime - 604800  # 604800 = 1 week period
    data = {}
    for row in cur.execute(SELECT_PI_SENSOR_BETWEEN, (trayid, time_range, eTime)).fetchall():
        if row[0] in data:
            data[row[0]].append((row[1], row[2]))
        else:
            data[row[0]] = [(row[1], row[2])]
    runs = [item for item in cur.execute("""SELECT piId, start, stop FROM current_runs""")]

    startTimes = [None, None, None, None, None]
    data['temperature'] = [item for item in cur.execute("""SELECT measurements.val AS val, measurements.epoch_time AS etime 
                            FROM measurements
                            INNER JOIN active_nodes ON active_nodes.id = measurements.nodeId
                            INNER JOIN devices ON devices.id = active_nodes.devId
                            WHERE active_nodes.piId = 1 AND devices.device="temperature" AND etime BETWEEN ? and ?
                            ORDER BY etime;""", (1619238114, 1619269749))]

    external_temp = [item for item in cur.execute("""SELECT measurements.val AS val, measurements.epoch_time AS etime 
                            FROM measurements
                            INNER JOIN active_nodes ON active_nodes.id = measurements.nodeId
                            INNER JOIN devices ON devices.id = active_nodes.devId
                            WHERE active_nodes.piId = 0 AND devices.device="temperature" AND etime BETWEEN ? and ?
                            ORDER BY etime;""", (data['temperature'][0][1], data['temperature'][-1][1]))]

    data['ec'] = [item for item in cur.execute("""SELECT measurements.val AS val, measurements.epoch_time AS etime 
                            FROM measurements
                            INNER JOIN active_nodes ON active_nodes.id = measurements.nodeId
                            INNER JOIN devices ON devices.id = active_nodes.devId
                            WHERE active_nodes.piId = 1 AND devices.device="ec" AND etime BETWEEN ? and ?
                            ORDER BY etime;""", (1619062979, 1619195473))]

    data['ph'] = [item for item in cur.execute("""SELECT measurements.val AS val, measurements.epoch_time AS etime 
                            FROM measurements
                            INNER JOIN active_nodes ON active_nodes.id = measurements.nodeId
                            INNER JOIN devices ON devices.id = active_nodes.devId
                            WHERE active_nodes.piId = 1 AND devices.device="ph" AND etime BETWEEN ? and ?
                            ORDER BY etime;""", (1619191817, 1619284373))]
    for item in runs:
        startTimes[item[0]-1] = round(100 * (eTime - item[1]) / (item[2]-item[1]+1), 1)
    conn.close()
    return render_template('tray.html', data=data, times=startTimes, trayId=trayid, external_temp=external_temp)


@main.route('/trayinfo/<trayid>/trayControl', methods=['GET', 'POST'])
def control(trayid):
    conn = connect()
    cur = conn.cursor()
    data = {item[0].replace(' ', '_'): item[1] for item in cur.execute(PI4_STATUS)}
    run = cur.execute(CHECK_RUN_EXISTS, (trayid,)).fetchone()
    conn.close()
    return render_template('trayCtrl.html', status=data, trayId=trayid, exists=run)


@main.route('/trayinfo/<trayid>/trayControl/newGrow', methods=['GET', 'POST'])
def newCycle(trayid):
    if request.form['microgreen']:
        tray_start(trayid, request.form['microgreen'])
    return redirect("/")