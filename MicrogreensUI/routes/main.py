from flask import Blueprint, render_template, json, \
    redirect, request, url_for
from server.mongoDB import tray_data, status

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/', methods=['GET', 'POST'])
def index():
    for item in status.find({}, {'id:': 0}):
        print(item)
    return render_template('index.html', status=status.find({}, {'id:': 0}))


@main.route('/settings', methods=['GET', 'POST'])
def settings():
    return render_template('index.html')


@main.route('/trayinfo/<trayid>', methods=['GET', 'POST'])
def data(trayid):
    ph_data = tray_data.find({'tray': int(trayid), 'sensor': 'ph'}, {'_id': 0 })
    weight_data = tray_data.find({'tray': int(trayid), 'sensor': 'ph'}, {'_id': 0 })
    water_data = tray_data.find({'tray': int(trayid), 'sensor': 'water level'}, {'_id': 0 })
    return render_template('tray.html', ph=ph_data, weight=weight_data, water=water_data)

# eli was here
# Daniel replies back!