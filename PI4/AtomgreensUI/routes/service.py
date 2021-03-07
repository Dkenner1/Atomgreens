from flask import Blueprint, render_template, jsonify, request
import random
from util.db import connect
from util.SQL import *
import time

service_routes = Blueprint('service', __name__, template_folder='templates')


@service_routes.route('/service', methods=['GET', 'POST'])
def service():
    return render_template('service.html', alerts={"water_lvl"})


@service_routes.route('/service/diag', methods=['GET', 'POST'])
def diagnostic_start():
    return jsonify(run_test())


@service_routes.route('/service/poll', methods=['GET', 'POST'])
def poll():
    print("Polling endpoint!")
    if switcher():
        return jsonify({"water_level": 15})
    return jsonify({"water_level": 50})


@service_routes.route('/service/setting_update', methods=['GET', 'POST'])
def update_setting():
    print(request.form)
    return ('', 204)


def run_test():
    print("Diagnosing the device!")
    return {"stranger danger": True, "Line Break": False, "Macaroon theft": True}


def switcher():
    return random.randint(0, 2)
