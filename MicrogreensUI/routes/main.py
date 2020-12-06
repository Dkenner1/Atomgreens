from flask import Blueprint, render_template, json, \
    redirect, request, url_for
from server.mongoDB import tray_data, status

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/', methods=['GET', 'POST'])
def index():
    #mongodb query {item['sensor']: item['value'] for item in status.find({'tray': 1}, {'_id:': 0})}
    data = {'tray_status': [{'id': 1, 'iscomplete': True}, {'id': 1, 'iscomplete': False}, {'id': 3, 'iscomplete': False},  {'id': 4, 'iscomplete': True}], 'water_level': 11}
    return render_template('index.html', status=data)


@main.route('/settings', methods=['GET', 'POST'])
def settings():
    return render_template('index.html')


@main.route('/trayinfo/<trayid>', methods=['GET', 'POST'])
def data(trayid):
    ph_data = tray_data.find({'tray': int(trayid), 'sensor': 'ph'}, {'_id': 0})
    weight_data = tray_data.find({'tray': int(trayid), 'sensor': 'ph'}, {'_id': 0})
    water_data = tray_data.find({'tray': int(trayid), 'sensor': 'water level'}, {'_id': 0})
    return render_template('tray.html', ph=ph_data, weight=weight_data, water=water_data)

# eli was here
# Daniel replies back!
