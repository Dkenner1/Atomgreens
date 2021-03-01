import RPi.GPIO as GPIO
from time import sleep
import serial
import configparser 
from EventHub import eventHub
from listener import listen
import utcp
import pwm_callable
import weight_sensor
import Temp_and_humidity_sensor
import Solinoid


ser = serial.Serial(port="/dev/serial0", baudrate=9600)  # Open port with baud rate
sender = UTCP(ser)
listen(ser, ser)


eventHub.subscribe(Temp_and_humidity_sensor.TH.read_temp_humidity, 1)
eventHub.subscribe(Temp_and_humidity_sensor.TH.read_temp_humidity, 2)
eventHub.subscribe(weight_sensor, 3)
eventHub.subscribe(Solinoid, 4)
eventHub.subscribe(pwm_callable.setPWM.recive, 5)
eventHub.subscribe(pwm_callable.setPWM.recive, 6)

