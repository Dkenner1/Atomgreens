import serial
from utcp import UTCP
from listener import listen
from EventHub import eventHub
from behaviors import *
from time import sleep

ser = serial.Serial(port="/dev/serial0", baudrate=9600)  # Open port with baud rate
sender = UTCP(ser)
listen(ser, ser)

eventHub.subscribe(store, 'DEFAULT')
sleep(2)
#turn off red 
sender.send(1, 6, 0) # pi id, dev id, data
sleep(2)
#turn off blue
sender.send(1, 5, 0) # pi id, dev id, data
sleep(2)
#call the temp sensor
sender.send(1, 1, 0) # pi id, dev id, data
sleep(2)
#turn on actuator
sender.send(1, 4, 1) # pi id, dev id, data
sleep(2)


