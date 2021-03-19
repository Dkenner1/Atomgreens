import serial
from utcp import UTCP
from listener import listen
from EventHub import eventHub
from behaviors import *

ser = serial.Serial(port="/dev/serial0", baudrate=9600)  # Open port with baud rate
sender = UTCP(ser)
listen(ser, ser)

eventHub.subscribe(store, 'DEFAULT')

sender.send(1, 2, 1 ) # pi id, dev id, data
    
