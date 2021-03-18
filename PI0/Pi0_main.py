import RPi.GPIO as GPIO
from time import sleep
import serial
from EventHub import eventHub
from listener import listen
from behaviors import *
import pwm_callable
# from weight_sensor import w_sensor
import Temp_and_humidity_sensor_pi0
# from Solinoid import pwm
# import json
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32,GPIO.OUT) #turns on blue lights
GPIO.output(32, GPIO.HIGH)

ser = serial.Serial(port="/dev/ttyAMA0", baudrate=9600)  # Open port with baud rate
listen(ser, ser)

eventHub.subscribe(updatePiID, 'FLAGS')
eventHub.subscribe(fwd, 'FWD')
eventHub.subscribe(Temp_and_humidity_sensor_pi0.TH.read_temp_humidity, 3)
eventHub.subscribe(Temp_and_humidity_sensor_pi0.TH.read_temp_humidity, 4)
# eventHub.subscribe(w_sensor.weight, 3)
# eventHub.subscribe(pwm.recive, 4)
# eventHub.subscribe(pwm_callable.setPWM.recive, 5)
# eventHub.subscribe(pwm_callable.setPWM.recive, 6)

GPIO.setup(33,GPIO.OUT) #turns on red lights 
GPIO.output(33, GPIO.HIGH)

