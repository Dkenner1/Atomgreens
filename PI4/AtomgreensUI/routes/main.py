from flask import Blueprint, render_template, json, \
    redirect, request, url_for
from util.db import connect
from util.SQL import *
import time

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/', methods=['GET', 'POST'])
def index():
    conn = connect()
    cur = conn.cursor()
    data = {item[0].replace(' ', '_'): item[1] for item in cur.execute(PI4_STATUS)}
    conn.close()
    print("Page data: " + str(data))
    return render_template('index.html', status=data)


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
    conn.close()
    for i in data:
        print(i)
        print(i, data[i])
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template('tray.html', data=data, labels=labels, values=values)


@main.route('/trayinfo/<trayid>/trayControl', methods=['GET', 'POST'])
def control(trayid):
    print("We got here!")
    conn = connect()
    cur = conn.cursor()
    data = {item[0].replace(' ', '_'): item[1] for item in cur.execute(PI4_STATUS)}
    conn.close()
    print("Page data: " + str(data))
    return render_template('trayCtrl.html', data=data)
