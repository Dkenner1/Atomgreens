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
    DCTEC = 31
    fan = 33
    heater = 37

    GPIO.setup(DCTEC, GPIO.OUT)
    GPIO.setup(fan, GPIO.OUT)
    GPIO.setup(heater, GPIO.OUT)
    
    @threaded
    def control():
        # Query database for last stored temperature value of tray 4
        conn = connect()
        cur = conn.cursor()
        data = {item[0].replace('', '_'): item[1] for item in cur.execute(PI4_STATUS)}
        conn.close()
        # Store temp value as local file variable, curTemp | Question: Conversion necessary?
        curTemp = data['temp']

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
            # After diff minutes, turn off heater and fan for the "difference amount" of minutes
            GPIO.output(heater, GPIO.LOW)
            GPIO.output(fan, GPIO.LOW)
            # Question: Call temperature sensor for reading after diff minutes or wait for 10 minute timer and repeat climate control procedure?

        if curTemp > overTemp
            # Determine difference from curTemp and overTemp
            onMinutes =  curTemp - overTemp
            if (onMinutes > 9.8): #we call this file every 10 min therefore this cannot last more then 10 min 
                onMinutes = 9.8 #sleeps for the correct amount of seconds 
            onMinutes = round(onMinutes*60)

            # Turn on TEC cooler, DC peristaltic pump and fan for the "difference amount" of minutes
            GPIO.output(DCTEC, GPIO.HIGH)
            GPIO.output(fan, GPIO.HIGH)
            # After diff minutes, TEC cooler, DC peristaltic pump and fan off
            sleep(onMinutes)
            GPIO.output(DCTEC, GPIO.HIGH)
            GPIO.output(fan, GPIO.HIGH)
            # Question: Call temperature sensor for reading after diff minutes or wait for 10 minute timer and repeat climate control procedure?



