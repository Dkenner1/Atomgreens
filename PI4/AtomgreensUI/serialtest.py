
from serial.utcp import UTCP
from serial.listener import listen
from util.EventHub import eventHub
from serial.behaviors import *
from time import sleep

import devices.Temp_and_humidity_sensor_pi4
import devices.climate_control


Temp_and_humidity_sensor_pi4.read_temp_humidity()




# ser = serial.Serial(port="/dev/serial0", baudrate=9600)  # Open port with baud rate
# sender = UTCP(ser)
# listen(ser, ser)
# 
# eventHub.subscribe(store, 'DEFAULT')
# sleep(2)
# #turn off red 
# sender.send(1, 6, 0) # pi id, dev id, data
# sleep(2)
# #turn off blue
# sender.send(1, 5, 0) # pi id, dev id, data
# sleep(2)
# #call the temp sensor
# sender.send(1, 1, 0) # pi id, dev id, data
# sleep(2)
# #turn on actuatossh r
# sender.send(1, 4, 0) # pi id, dev id, data
# sleep(2)
# 

