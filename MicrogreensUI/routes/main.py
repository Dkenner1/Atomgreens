from flask import Blueprint, render_template, json, \
    redirect, request, url_for
from util.db import query
import time

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/', methods=['GET', 'POST'])
def index():
    queryStr = """SELECT sensor, value, MAX(epoch_time) AS time  FROM data GROUP BY sensor"""
    data = query('atomgreens', queryStr)
    return render_template('index.html', status=data)


@main.route('/settings', methods=['GET', 'POST'])
def settings():
    return render_template('index.html')


@main.route('/trayinfo/<trayid>', methods=['GET', 'POST'])
def data(trayid):
    etime = time.time()
    time_range = etime-604800 # 1 week period
    queryStr = "SELECT * FROM data WHERE time >=" + str(time_range)
    result = query(queryStr)
    return render_template('tray.html')

@main.route('/service', methods=['GET', 'POST'])
def service():
    return render_template('service.html')

# eli was here
# Daniel replies back!
