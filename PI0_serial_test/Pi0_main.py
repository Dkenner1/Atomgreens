import RPi.GPIO as GPIO
from time import sleep
import serial
import configparser 
from EventHub import eventHub
from listener import listen
from utcp import UTCP
import pwm_callable
from weight_sensor import w_sensor
import Temp_and_humidity_sensor
from Solinoid import pwm
import json

ser = serial.Serial(port="/dev/serial0", baudrate=9600)  # Open port with baud rate
sender = UTCP(ser)
listen(ser, None)


def updatePiID(msg=None):
    if  msg['msg']['flags'] == 1:
        with open('msg_config.json') as jfile:
            x=json.load(jfile)
            x['piID'] = msg['msg']['msg']
        with open('msg_config.json', 'w') as jfile:
            json.dump(x, jfile, indent=4)
            
eventHub.subscribe(updatePiID, "FLAGS")
eventHub.subscribe(Temp_and_humidity_sensor.TH.read_temp_humidity, 1)
eventHub.subscribe(Temp_and_humidity_sensor.TH.read_temp_humidity, 2)
eventHub.subscribe(w_sensor.weight, 3)
eventHub.subscribe(pwm.recive, 4)
eventHub.subscribe(pwm_callable.setPWM.recive, 5)
eventHub.subscribe(pwm_callable.setPWM.recive, 6)
