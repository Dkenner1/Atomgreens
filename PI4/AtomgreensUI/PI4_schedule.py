import schedule
import time
from time import sleep
import serial
from serial.utcp import UTCP
from serial.listener import listen
from util.EventHub import eventHub
#from behaviors import *  #you might not need this file
from database.db import connect
from database.db import add_meas
from database.SQL import * 

import devices.Temp_and_humidity_sensor_pi4
import devices.Water_level
import devices.ph_ec_sensors
import devices.water_pump_ctrl
import devices.ph_ec_pump
import devices.climate_control

ser = serial.Serial(port="/dev/serial0", baudrate=9600)  # Open port with baud rate
sender = UTCP(ser)
listen(ser, ser)
global solOn
solOn = 0

def Pi0All(devid, data):
    #sender.send(piID, devID, Data)
    sleep(2)
    sender.send(1, devid, data) # get the temp and humidity sensor data from the 1st pi0
    sleep(2)
    #sender.send(2, devid, data) # 2nd pi0
    #sleep(.5)
    #sender.send(3, devid, data) # 3rd pi0
    #sleep(.5)
    #sender.send(4, devid, data) # 4th pi0
    #sleep(.5)
    #sender.send(5, devid, data) # 5th pi0
    #sleep(.5)

def LEDon():
    #get LED intesnity Data
    '''
    Red = [0,0,0,0,0]
    Blue = [0,0,0,0,0]
    on = [0,0,0,0,0]
    conn = connect()
    cur = conn.cursor()
    conn.close()
    for x in range(5):
        for row in cur.execute('SELECT val, MAX(epoch_time) FROM STATUS WHERE piID = ? and devid = 17', str(x)): #Determine if the tray is active 
            on[x] = row
        for row in cur.execute('SELECT val, MAX(epoch_time) FROM STATUS WHERE piID = ? and devid = 5', str(x)): #if the tray is active, turn on the red lights 
            if (on[x][0] >= 1): #if the tray is on then turn on the red lights
                Red[x] = row
                sender.send(x, 5, Red[x][0]) #sender.send(piID, devID, Data)
        for row in cur.execute('SELECT val, MAX(epoch_time) FROM STATUS WHERE piID = ? and devid = 6', str(x)): #if the tray is active, turn on the Blue lights
            if (on[x][0] >= 1): #if the tray is on then turn on the red lights
                Blue[x] = row
                sender.send(x, 6, Blue[x][0]) #sender.send(piID, devID, Data)
    conn.close()
    '''
    print('LED on')
    Pi0All(5, 80) #turn on the Red LEDs to 80%
    Pi0All(6, 50) #turn on the Blue LEDs to 50%
    
def LEDoff():
    print('LED off')
    Pi0All(5, 0)
    Pi0All(6, 0) 
    
def water():
    '''
    on = [0,0,0,0,0]
    conn = connect()
    cur = conn.cursor()
    for x in range(5): #turn on the solinoids
        for row in cur.execute('SELECT val, MAX(epoch_time) FROM STATUS WHERE piID = ? and devid = 17', str(x)): #get the latest temp value 
            on[x] = row
            if (on[x][0] >= 1):
                sender.send(x, 4, 1) #sender.send(piID, devID, Data)
    conn.close()
    '''
    print('Water')
    Pi0All(4, 1) #turn on the solinoids (replace this with the above code)
    global solOn
    solOn = 1
    water_pump_ctrl.water(1) #turn on the air and water pump 
    #ph_ec_sensors.PH_EC.readPHEC() #read the water temp, ph, and ec

def scheduler(): #run every 10 minutes - have all of the sensor files run
    print('Scheduler')
    #Temp_and_humidity_sensor_pi4.read_temp_humidity() #get the temp and humidity data from the breakout board 
    Pi0All(1, 0) # get the temp and humidity data from all of the pi0s
    #Pi0All(3, 5) # get the weight data from all PI0's 
    #Water_level.read_waterLevel() #get the water level
    
    global solOn
    #actuators
    print(solOn)
    if (solOn == 0): #check to see if the solinoids should be shut
        Pi0All(4, 0) #turn off the solinoids
        print('turn off solinoids')
        #ph_ec_pump.PhEcPump.On() #activate the PH and EC pump in order to keep the level constent in the water
        #pump turns off in the PH_EC_pump file
        # Delete when adding the PH and EC stuff in the loop 
        water_pump_ctrl.water(0)
    else:
        print('Itorate for solinoids')
        solOn = solOn - 1 # determines if we have waited the right amount of time 
    #climate_control.control() #activate climate control for this chunk of time 
   
def call():
    schedule.every(2).minutes.do(water) #every hour, find which trays should be open and turn them on for the correct amount of time
    schedule.every(1).minutes.do(scheduler) #every 10 min get data
    schedule.every().day.at("21:00").do(LEDon)
    schedule.every().day.at("13:00").do(LEDoff)

    while True:
        schedule.run_pending()
        time.sleep(60) #checks every minute 







