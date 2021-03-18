# water_pump.py

import RPi.GPIO as GPIO
from time import sleep
#from util.db import connect, add_meas
#from util.SQL import PI4_STATUS

class WaterPumpCtrl:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    # GPIO pin for water pump
    waterPump = 8
    GPIO.setup(waterPump, GPIO.OUT)

    # GPIO pin for water level sensor
    waterLevel = 23
    GPIO.setup(waterSensor, GPIO.IN)

    def water_On(waterLevel, waterPump):
        if GPIO.input(waterLevel):
            # print("Water Pump: On")add_meas(1, 9, (pumpCnt + ecPumpCount))
            GPIO.output(waterPump, GPIO.HIGH)
            add_meas(1, 14, 1) #tell the database that the water level is okay 
            
