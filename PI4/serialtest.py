import serial
from utcp import UTCP
from listener import listen
from EventHub import eventHub
from behaviors import *

ser = serial.Serial(port="/dev/serial0", baudrate=9600)  # Open port with baud rate
sender = UTCP(ser)
listen(ser, ser)

eventHub.subscribe(store, 'DEFAULT')

#turn on blue lights
sender.send(1, 5, 20) # pi id, dev id, data
sleep(2)
#turn on red lights
sender.send(1, 6, 20) # pi id, dev id, data
sleep(2)
#turn on actuator
sender.send(1, 4, 1) # pi id, dev id, data
sleep(2)
#turn off actuator
sender.send(1, 4, 0) # pi id, dev id, data
sleep(2)
