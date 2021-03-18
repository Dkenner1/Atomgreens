import serial
from utcp import UTCP
from listener import listen
from EventHub import eventHub
from behaviors import *

ser = serial.Serial(port="/dev/serial0", baudrate=9600)  # Open port with baud rate
sender = UTCP(ser)
listen(ser, ser)

eventHub.subscribe(store, 'DEFAULT')

if __name__ == '__main__':
    sender.send(0, 1, 5) # pi id, dev id, data
    