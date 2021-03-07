# Neccesaey libraries and functions from app.py to run start_server
from flask import Flask
from routes import main, service
import logging, threading
from waitress import serve

from AtomgreensUI.app import start_server
import PI4_sensor_scheduler

threading.Thread(target=start_server())
PI4_sensor_scheduler.schedule.call()