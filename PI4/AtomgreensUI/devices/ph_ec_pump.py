import RPi.GPIO as GPIO
from time import sleep
from database.db import connect, add_meas
from database.SQL import PI4_STATUS
from util.util import threaded
from devices.water_pump_ctrl import *

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

SPR = 200 # Steps per revolution
delay = 0.027

pinPHBlack = 40
pinPHGrn = 38
pinPHBlue = 32
pinPHRed = 36

pinECBlack = 37
pinECGrn = 35
pinECBlue = 31
pinECRed = 33

CTRL = 29

control_pins = [pinPHBlack, pinPHGrn, pinPHBlue, pinPHRed, pinECBlack, pinECGrn, pinECBlue, pinECRed, CTRL]
for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)
GPIO.output(29, GPIO.LOW) #turns off both pumps

# Placeholder values, find and insert new values here with testing 
stdValPH = 5.5
stdValEC = 250

# initalizing values 
phPumpCount = 0
ecPumpCount = 0
#add_meas(1, 11, 5.7) #inserting origonal PH value
#add_meas(1, 12, 220) #inserting origonal EC value 

@threaded
def On():
    conn = connect()
    cur = conn.cursor()
    for row in cur.execute('SELECT measurements.val, MAX(measurements.epoch_time) FROM measurements INNER JOIN nodes ON measurements.nodeId=nodes.id WHERE nodes.piId=1 AND nodes.devId=11'): #get the latest temp value
        phVal = row
    for row in cur.execute('SELECT measurements.val, MAX(measurements.epoch_time) FROM measurements INNER JOIN nodes ON measurements.nodeId=nodes.id WHERE nodes.piId=1 AND nodes.devId=12'): #get the latest temp value
        ecVal = row
    for row in cur.execute('SELECT measurements.val, MAX(measurements.epoch_time) FROM measurements INNER JOIN nodes ON measurements.nodeId=nodes.id WHERE nodes.piId=1 AND nodes.devId=10'): #get the latest temp value
        phPumpCtDB = row
    for row in cur.execute('SELECT measurements.val, MAX(measurements.epoch_time) FROM measurements INNER JOIN nodes ON measurements.nodeId=nodes.id WHERE nodes.piId=0 AND nodes.devId=9'): #get the latest temp value
        ecPumpCtDB = row
    conn.close()

    phVal = int(phVal[0])
    ecVal = int(ecVal[0])
    phPumpCtDB = int(phPumpCtDB[0])
    ecPumpCtDB = int(ecPumpCtDB[0])
    

    GPIO.output(29, GPIO.HIGH) #turn on the pumps
    # If below cutoff, turn on respective pumps, increment pump count and write pump count value to database
    # PH pump
    if ((phVal < (stdValPH-.2)) and (phPumpCtDB > 1)):
        runPH = ((phVal - stdValPH) * 10) * SPR
        phPumpCount = ((phVal - stdValPH) * 10)/2 #percentage of stuff used in this round
        add_meas(1,10,(phPumpCtDB - phPumpCount))
        # Turn on PH pump
        for x in range(round(runPH)):
                GPIO.output(pinECBlack, GPIO.LOW)
                GPIO.output(pinECRed, GPIO.HIGH)
                sleep(delay)
                GPIO.output(pinECRed, GPIO.LOW)
                GPIO.output(pinECGrn, GPIO.HIGH)
                sleep(delay)
                GPIO.output(pinECGrn, GPIO.LOW)
                GPIO.output(pinECBlue, GPIO.HIGH)
                sleep(delay)
                GPIO.output(pinECBlue, GPIO.LOW)
                GPIO.output(pinECBlack, GPIO.HIGH)
                sleep(delay)
    GPIO.output(pinPHGrn, GPIO.LOW)
    GPIO.output(pinPHBlue, GPIO.LOW)
    GPIO.output(pinPHGrn, GPIO.LOW)
    GPIO.output(pinPHBlue, GPIO.LOW)
    # Increment phPumpCount and insert phPumpCount value into database | Question: add_meas() function to be used?
    

    # EC pump
    if (ecVal < (stdValEC - 10) and ecVal > 5 and (ecPumpCtDB > 1)):
        runEC = ((stdValEC - ecVal)/10) * SPR
        ecPumpCount = ((stdValEC - ecVal) * 10)/2
        add_meas(1, 9, (ecPumpCtDB - ecPumpCount))
        # Turn on EC pump
        for x in range(round(runEC)):
            GPIO.output(pinECBlack, GPIO.LOW)
            GPIO.output(pinECRed, GPIO.HIGH)
            sleep(delay)
            GPIO.output(pinECRed, GPIO.LOW)
            GPIO.output(pinECGrn, GPIO.HIGH)
            sleep(delay)
            GPIO.output(pinECGrn, GPIO.LOW)
            GPIO.output(pinECBlue, GPIO.HIGH)
            sleep(delay)
            GPIO.output(pinECBlue, GPIO.LOW)
            GPIO.output(pinECBlack, GPIO.HIGH)
            sleep(delay)
    GPIO.output(pinECBlack, GPIO.LOW) #turn off all of the leads
    GPIO.output(pinECRed, GPIO.LOW)
    GPIO.output(pinECGrn, GPIO.LOW)
    GPIO.output(pinECBlue, GPIO.LOW)
    # Increment ecPumpCount and insert ecPumpCount value into database | Question: add_meas() function to be used?
    GPIO.output(29, GPIO.LOW) #turn off the pumps

    sleep(5)
    water_pump_ctrl.water(0) #turn off the water & air pump
