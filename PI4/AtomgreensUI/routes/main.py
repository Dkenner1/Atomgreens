from flask import Blueprint, render_template, json, \
    redirect, request, url_for
from util.db import connect
from util.SQL import *
import time
import datetime

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/', methods=['GET', 'POST'])
def index():
    conn = connect()
    cur = conn.cursor()
    data = {item[0].replace(' ', '_'): item[1] for item in cur.execute(PI4_STATUS)}
    eTime = time.time()
    day = 86400
    hour = 3600
    now = datetime.date.today()
    startTimes = [int(((now - (datetime.date.fromtimestamp((eTime - 2 * day - 5 * hour)))).days / 7) * 100),
                  int(((now - (datetime.date.fromtimestamp((eTime - 3 * day - 2 * hour)))).days / 7) * 100),
                  int(((now - (datetime.date.fromtimestamp((eTime - 1 * day - 0 * hour)))).days / 7) * 100),
                  int(((now - (datetime.date.fromtimestamp((eTime - 4 * day - 5 * hour)))).days / 7) * 100),
                  int(((now - (datetime.date.fromtimestamp((eTime - 5 * day - 2 * hour)))).days / 7) * 100)]
    conn.close()
    print("Page data: " + str(data))
    return render_template('index.html', status=data, times=startTimes)


@main.route('/trayinfo/<trayid>', methods=['GET', 'POST'])
def data(trayid):
    conn = connect()
    cur = conn.cursor()
    etime = time.time()
    time_range = etime - 604800  # 1 week period
    data = {}
    for row in cur.execute(SELECT_PI_SENSOR_BETWEEN, (trayid, time_range, etime)).fetchall():
        if row[0] in data:
            data[row[0]].append((row[1], row[2]))
        else:
            data[row[0]] = [(row[1], row[2])]

    eTime = time.time()
    day = 86400
    hour = 3600
    now = datetime.date.today()
    startTimes = [int(((now - (datetime.date.fromtimestamp((eTime - 2 * day - 5 * hour)))).days / 7) * 100),
                  int(((now - (datetime.date.fromtimestamp((eTime - 3 * day - 2 * hour)))).days / 7) * 100),
                  int(((now - (datetime.date.fromtimestamp((eTime - 1 * day - 0 * hour)))).days / 7) * 100),
                  int(((now - (datetime.date.fromtimestamp((eTime - 4 * day - 5 * hour)))).days / 7) * 100),
                  int(((now - (datetime.date.fromtimestamp((eTime - 5 * day - 2 * hour)))).days / 7) * 100)]
    conn.close()
    return render_template('tray.html', data=data, times=startTimes)


@main.route('/trayinfo/<trayid>/trayControl', methods=['GET', 'POST'])
def control(trayid):
    print("We got here!")
    conn = connect()
    cur = conn.cursor()
    data = {item[0].replace(' ', '_'): item[1] for item in cur.execute(PI4_STATUS)}
    conn.close()
    print("Page data: " + str(data))
    return render_template('trayCtrl.html', status=data)
