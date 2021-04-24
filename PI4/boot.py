# Neccesaey libraries and functions from app.py to run start_server
# from flask import Flask
# from routes import main, service
# import logging, threading
# from waitress import serve
from time import sleep

# from AtomgreensUI.app import start_server
import PI4_schedule
import Stop
# sleep(1)
Stop.off() #turns off all of the GPIO in order to prevent undesired premature function
#threading.Thread(target=start_server())
sleep(1)
PI4_schedule.call()
