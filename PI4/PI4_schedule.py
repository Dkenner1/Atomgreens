import schedule
import time
import serial
from utcp import UTCP
from listener import listen
from EventHub import eventHub
from behaviors import *  #you might not need this file
from util.db import connect
from util.SQL import *

import Temp_and_humidity_sensor_pi4
import Water_level
import ph_ec_sensors
import water_pump_ctrl
import ph_ec_pump
import climate_control

ser = serial.Serial(port="/dev/serial0", baudrate=9600)  # Open port with baud rate
sender = UTCP(ser)
listen(ser, ser)
solOn = 0

''' #an idealiation on how to get the data from the database 
def getLast(devId, piId):
    result = cur.execute(SELECT_NODEID, (piId, devId)).fetchone()
    if result:
        id = result[0]
    string = 'LAST_VALUE('+str(id)+')'
    data = query(string)
    return data 
'''

def serial(devid, data):
    #sender.send(piID, devID, Data)
    sender.send(1, devid, data) # get the temp and humidity sensor data from the 1st pi0
    sender.send(2, devid, data) # 2nd pi0
    #sender.send(3, devid, data) # 3rd pi0
    #sender.send(4, devid, data) # 4th pi0
    #sender.send(5, devid, data) # 5th pi0

def schedule(): #run every 10 minutes - have all of the sensor files run
    Temp_and_humidity_sensor_pi4.TH.read_temp_humidity() #get the temp and humidity data from the breakout board 
    serial(1, 5) # get the temp and humidity data from all of the pi0s 
    serial(3, 5) # get the weight data from all PI0's 
    Water_level.waterLevel.read_waterLevel() #get the waver level
    
    
    #actuators
    if (solOn == 0): #check to see if the solinoids should be shut
        serial(4, 0) #turn off the solinoids
        #ph_ec_pump.PhEcPump.On() #activate the PH and EC pump in order to keep the level constent in the water
        #pump turns off in the PH_EC_pump file
        # Delete when adding the PH and EC stuff in the loop 
        water_pump_ctrl.WaterPumpCtrl.water(0) 
    else:
        solOn = solOn - 1 # determines if we have waited the right amount of time 
    #climate_control.ClimateCtrl.control() #activate climate control for this chunk of time 
    

def LEDon():
    #get LED intesnity Data
    '''
    for x in range(5):
        if (#call DB for trayActive?):
            sender.send(x, 5, #call DB for LED intensity)
            sender.send(x, 6, #call DB for LED intensity)
    '''
    serial(5, 80) #turn on the RED LEDs to 80
    serial(6, 50) #turn on the RED LEDs to 50
    
def LEDoff():
    serial(5, 0)
    serial(6, 0) 
    
def water():
    serial(4, 1) #turn on the solinoids
    solOn = 1
    water_pump_ctrl.WaterPumpCtrl.water(1) #turn on the air and water pump 
    #ph_ec_sensors.PH_EC.readPHEC() #read the water temp, ph, and ec
    '''
    for x in range(5):
        if (#call DB for trayActive?):
            sender.send(x, 4, #call DB for duration)
    '''
    
schedule.every(60).minutes.do(water) #every hour, find which trays should be open and turn them on for the correct amount of time
schedule.every(10).seconds.do(schedule) #every 10 min get data
schedule.every().day.at("21:00").do(LEDon)
schedule.every().day.at("13:00").do(LEDoff)

while True:
    schedule.run_pending()
    time.sleep(60) #checks ever minute 







