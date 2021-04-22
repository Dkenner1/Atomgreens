import schedule
import time
from time import sleep
import serial
from utcp import UTCP
from listener import listen
from EventHub import eventHub
from behaviors import *  #you might not need this file
from database.db import connect
from database.db import add_meas
from database.SQL import * 

import Temp_and_humidity_sensor_pi4
import Water_level
import ph_ec_sensors
import water_pump_ctrl

import ph_ec_pump
import climate_control

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
    conn = connect()
    cur = conn.cursor()
    for row in cur.execute('SELECT state FROM flags'): #determine if we are in maintenence mode
        flag = row
    conn.close()

    if (flag[0] == 0): 
        print('LED on')
        #get LED intesnity Data
        off = [0,0,0,0,0]
        conn = connect()
        cur = conn.cursor()
        for x in range(5): #turn on the solinoids
            for row in cur.execute('SELECT stop, red, blue, start FROM current_runs WHERE piId=?', str(x)): #get the tray epoch time and type of microgreen
                off[x] = row
                red = off[x][1]
                blue = off[x][2]
                start = off[x][3]
                #if the current time is before the stop time and after the blackout period then turn on the LEDs
                if (time.time() < off[x][0] and time.time() > start+86400*2):  
                    sleep(.5)
                    sender.send(x, 5, red) #(piID, devID, Data) turn on red to desired intensity 
                    sleep(.5)
                    sender.send(x, 6, blue) # turn on blue to desired intensity 
                    sleep(.5)
        conn.close()
    
def LEDoff():
    print('LED off')
    Pi0All(5, 0)
    Pi0All(6, 0) 
    
def water():
    conn = connect()
    cur = conn.cursor()
    for row in cur.execute('SELECT state FROM flags'): #determine if we are in maintenence mode
        flag = row
    conn.close()

    if (flag[0] == 0): 
        print('Water')
        off = [0,0,0,0,0]
        active = 0
        conn = connect()
        cur = conn.cursor()
        for x in range(5): #turn on the solinoids
            for row in cur.execute('SELECT stop FROM current_runs WHERE piId=?', str(x)): #get the tray epoch time and type of microgreen
                off[x] = row
                if (time.time() < off[x][0]): #if the current time is before the stop time then open the solinoids.
                    sender.send(x, 4, 1) #sender.send(piID, devID, Data)
                    active = 1
        conn.close()

        #Pi0All(4, 1) #turn on the solinoids (replace this with the above code)
        if (active): #if at least one solinoid opens
            global solOn
            solOn = 1 #leave water on for x*10 minutes
            water_pump_ctrl.water(1) #turn on the air and water pump 
    

def scheduler(): #run every 10 minutes - have all of the sensor files run
    print('Scheduler')
    Temp_and_humidity_sensor_pi4.read_temp_humidity() #get the temp and humidity data from the breakout board 
    Pi0All(1, 0) # get the temp and humidity data from all of the pi0s
    #Pi0All(3, 5) # get the weight data from all PI0's 
    Water_level.read_waterLevel() #get the water level
    
    global solOn
    #actuators
    print(solOn)
    if (solOn == 0): #check to see if the solinoids should be shut
        Pi0All(4, 0) #turn off the solinoids
        print('turn off solinoids')
        ph_ec_sensors.readPHEC() #read the water temp, ph, and ec
        ph_ec_pump.On() #activate the PH and EC pump in order to keep the level constent in the water
        #pump turns off in the PH_EC_pump file
        # Delete when adding the PH and EC stuff in the loop 
        #water_pump_ctrl.water(0)
    else:
        print('Itorate for solinoids')
        solOn = solOn - 1 # determines if we have waited the right amount of time 
    #climate_control.control() #activate climate control for this chunk of time 
   
def call():
    schedule.every(1).minutes.do(scheduler) #every 10 min get data
    schedule.every(2).minutes.do(water) #every hour, find which trays should be open and turn them on for the correct amount of time
    schedule.every().day.at("21:00").do(LEDon)
    schedule.every().day.at("13:00").do(LEDoff)

    while True:
        schedule.run_pending()
        time.sleep(60) #checks every minute 







