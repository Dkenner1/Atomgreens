import schedule
import time
import serial
from utcp import UTCP
from listener import listen
from EventHub import eventHub
from behaviors import *  #you might not need this file
import Temp_and_humidity_sensor_pi4

ser = serial.Serial(port="/dev/serial0", baudrate=9600)  # Open port with baud rate
sender = UTCP(ser)
listen(ser, ser)

def schedule(): #run every 10 minutes - have all of the sensor files run
    #sender.send(piID, devID, Data)
    Temp_and_humidity_sensor_pi4.TH.read_temp_humidity()
    sender.send(1, 1, 5) # get the temp and humidity sensor data from the 1st pi0
    sender.send(2, 1, 5) # 2nd pi0
    sender.send(3, 1, 5) # 3rd pi0
    sender.send(4, 1, 5) # 4th pi0
    sender.send(5, 1, 5) # 5th pi0
    
    
    
    
    







schedule.every(10).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(60)







