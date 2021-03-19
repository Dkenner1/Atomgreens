import schedule
import time
import serial
from utcp import UTCP
from listener import listen
from EventHub import eventHub
from behaviors import *  #you might not need this file
import Temp_and_humidity_sensor_pi4
import Water_level

ser = serial.Serial(port="/dev/serial0", baudrate=9600)  # Open port with baud rate
sender = UTCP(ser)
listen(ser, ser)

def serial(devid):
    sender.send(1, devid, 5) # get the temp and humidity sensor data from the 1st pi0
    sender.send(2, devid, 5) # 2nd pi0
    sender.send(3, devid, 5) # 3rd pi0
    sender.send(4, devid, 5) # 4th pi0
    sender.send(5, devid, 5) # 5th pi0


def schedule(): #run every 10 minutes - have all of the sensor files run
    #sender.send(piID, devID, Data)
    Temp_and_humidity_sensor_pi4.TH.read_temp_humidity()
    serial(1) # get the temp and humidity sensor data from all of the pi0s 
    serial(3) # get the temp and humidity sensor data from all of the pi0s
    Water_level.waterLevel.read_waterLevel()
    
    
    

schedule.every(60).minutes.do() #every hour, find which trays should be open and turn them on for the correct amount of time 
schedule.every(10).seconds.do(schedule) #every 10 min get data 
while True:
    schedule.run_pending()
    time.sleep(60)







