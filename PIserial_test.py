from time import sleep
from pymongo import MongoClient
import serial

db = MongoClient('atomgreens')
tble = db['data']
ser = serial.Serial("/dev/ttyS0", 9600)  # Open port with baud rate
while True:
    received_data = ser.read()  # read serial port
    data_left = ser.inWaiting()  # check for remaining byte
    tble.insert(received_data)