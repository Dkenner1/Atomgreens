from flask import Blueprint, render_template, json, \
    redirect, request, url_for
from database.db import connect, new_run
from database.SQL import *
from devices.trayCtrl import *
# from devices.Temp_and_humidity_sensor_pi4 import read_temp_humidity
# from devices.ph_ec_pump import On
import time
import datetime


main = Blueprint('main', __name__, template_folder='templates')


@main.route('/', methods=['GET', 'POST'])
def index():
    conn = connect()
    cur = conn.cursor()
    data = {item[0].replace(' ', '_'): item[1] for item in cur.execute(PI4_STATUS)}
    eTime = time.time()
    days = 60 * 60 * 24

    startTimes = [(round(100 * (eTime - item[1]) / (5 * days), 1)) for item in
                  cur.execute("""SELECT piId, start FROM current_runs""")]
    weights = {item[0]: item[2] for item in
               cur.execute("""SELECT piID, device, val FROM status WHERE device='weight'""")}
    temps = {item[0]: item[2] for item in
               cur.execute("""SELECT piID, device, val FROM status WHERE device='temperature'""")}
    hums = {item[0]: item[2] for item in
             cur.execute("""SELECT piID, device, val FROM status WHERE device='humidity'""")}

    conn.close()
    return render_template('index.html', status=data, times=startTimes, weights=weights, temps=temps, hums=hums)


@main.route('/trayinfo/<trayid>', methods=['GET', 'POST'])
def data(trayid):
    conn = connect()
    cur = conn.cursor()
    eTime = time.time()
    days = 60 * 60 * 24
    time_range = eTime - 604800  # 604800 = 1 week period
    data = {}
    for row in cur.execute(SELECT_PI_SENSOR_BETWEEN, (trayid, time_range, eTime)).fetchall():
        if row[0] in data:
            data[row[0]].append((row[1], row[2]))
        else:
            data[row[0]] = [(row[1], row[2])]

    runs = [item for item in cur.execute("""SELECT piId, start, stop FROM current_runs""")]
    startTimes = [(round(100 * (eTime - item[1]) / (item[2]-item[1]+1), 1)) for item in runs]
    conn.close()
    return render_template('tray.html', data=data, times=startTimes, trayId=trayid)


@main.route('/trayinfo/<trayid>/trayControl', methods=['GET', 'POST'])
def control(trayid):
    print("We got here!")
    conn = connect()
    cur = conn.cursor()
    data = {item[0].replace(' ', '_'): item[1] for item in cur.execute(PI4_STATUS)}
    conn.close()
    print("Page data: " + str(data))
    return render_template('trayCtrl.html', status=data, trayId=trayid)


@main.route('/trayinfo/<trayid>/trayControl/newGrow', methods=['GET', 'POST'])
def newCycle(trayid):
    if request.form['microgreen']:
        tray_start(trayid, request.form['microgreen'])
    return redirect("/")