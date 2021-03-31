import RPi.GPIO as GPIO
from time import sleep
from util.db import connect
from util.SQL import PI4_STATUS

class ClimateCtrl:
    # Constant variable declaration 
    idealTemp = 26.5
    underTemp = 24.5 # 26.5 - 2
    overTemp = 28.5 # 26.5 + 2

    GPIO.setmode(GPIO.BOARD)

    # GPIO pin for water pump
    DCTEC = 7
    fan = 11
    heater = 12

    GPIO.setup(DCTEC, GPIO.OUT)
    GPIO.setup(fan, GPIO.OUT)
    GPIO.setup(heater, GPIO.OUT)
    
    @threaded
    def control():
        # Query database for last stored temperature value of tray 4
        conn = connect()
        cur = conn.cursor()
        for row in cur.execute('SELECT val, MAX(epoch_time) FROM STATUS WHERE piID = 4 and devid = 2'): #get the latest temp value 
            curTemp = row
        conn.close()

        if curTemp < underTemp:
            # Determine difference from curTemp and underTemp
            onMinutes =  underTemp - curTemp
            if (onMinutes > 9.8): #we call this file every 10 min therefore this cannot last more then 10 min 
                onMinutes = 9.8
            onMinutes = round(onMinutes*60)

            # Turn on heater and fan
            GPIO.output(heater, GPIO.HIGH)
            GPIO.output(fan, GPIO.HIGH)
            sleep(onMinutes) #sleeps for the correct amount of seconds 
            # After diff minutes, turn off heater and fan 
            GPIO.output(heater, GPIO.LOW)
            GPIO.output(fan, GPIO.LOW)

        if curTemp > overTemp:
            # Determine difference from curTemp and overTemp
            onMinutes =  curTemp - overTemp
            if (onMinutes > 9.8): #we call this file every 10 min therefore this cannot last more then 10 min 
                onMinutes = 9.8 #sleeps for the correct amount of seconds 
            onMinutes = round(onMinutes*60)

            # Turn on TEC cooler, DC peristaltic pump and fan for the "difference amount" of minutes
            GPIO.output(DCTEC, GPIO.HIGH)
            GPIO.output(fan, GPIO.HIGH)
            # After diff minutes, turn off the TEC cooler, DC peristaltic pump and fan
            sleep(onMinutes)
            GPIO.output(DCTEC, GPIO.HIGH)
            GPIO.output(fan, GPIO.HIGH)



