import RPi.GPIO as GPIO
from time import sleep
from database.db import connect
from database.SQL import PI4_STATUS
from util import threaded 

# Constant variable declaration 
idealTemp = 26.5
underTemp = 24.5 # 26.5 - 2
overTemp = 28.5 # 26.5 + 2

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# GPIO pin for water pump
DCTEC = 7
fan = 11
heater = 12

GPIO.setup(DCTEC, GPIO.OUT)
GPIO.setup(fan, GPIO.OUT)
GPIO.setup(heater, GPIO.OUT)
    
# @threaded
def control():
    # Query database for last stored temperature value of tray 4
    conn = connect()
    cur = conn.cursor()
    for row in cur.execute('SELECT measurements.val, MAX(measurements.epoch_time) FROM measurements INNER JOIN nodes ON measurements.nodeId=nodes.id WHERE nodes.piId=1 AND nodes.devId=2'): #get the latest temp value 
        curTemp = row
    conn.close()
    
    print(curTemp)
    curTemp = int(curTemp[0])

    if curTemp < underTemp:
        # Determine difference from curTemp and underTemp
        onMinutes =  underTemp - curTemp
        if (onMinutes > 9.8): #we call this file every 10 min therefore this cannot last more then 10 min 
            onMinutes = 9.8
        onSeconds = round(onMinutes*60)

        # Turn on heater and fan
        GPIO.output(heater, GPIO.HIGH)
        GPIO.output(fan, GPIO.HIGH)
        sleep(onSeconds) #sleeps for the correct amount of seconds 
        # After diff minutes, turn off heater and fan 
        GPIO.output(heater, GPIO.LOW)
        GPIO.output(fan, GPIO.LOW)

    if curTemp > overTemp:
        print('this should print')
        # Determine difference from curTemp and overTemp
        onMinutes =  curTemp - overTemp
        if (onMinutes > 9.8): #we call this file every 10 min therefore this cannot last more then 10 min 
            onMinutes = 9.8 #sleeps for the correct amount of seconds 
        onSeconds = round(onMinutes*60)

        # Turn on TEC cooler, DC peristaltic pump and fan for the "difference amount" of minutes
        GPIO.output(DCTEC, GPIO.HIGH)
        GPIO.output(fan, GPIO.HIGH)
        # After diff minutes, turn off the TEC cooler, DC peristaltic pump and fan
        print(onSeconds)
        sleep(onSeconds)
        print('off')
        GPIO.output(DCTEC, GPIO.LOW)
        GPIO.output(fan, GPIO.LOW)



