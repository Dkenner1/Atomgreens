from flask import Blueprint, render_template, json, \
    redirect, request, url_for
import logging, os

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route('/settings', methods=['GET', 'POST'])
def settings():
    return render_template('index.html')


@main.route('/trayinfo/<dynamicid>', methods=['GET', 'POST'])
def data():
    return render_template('index.html')
