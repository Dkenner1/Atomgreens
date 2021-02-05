# water_pump.py

import RPi.GPIO as GPIO
from time import sleep

class waterpumpctrl:
    GPIO.setmode(GPIO.BOARD)

    # GPIO pin for water pump
    waterPump = 8
    GPIO.setup(waterPump, GPIO.OUT)

    # GPIO pin for water level sensor
    waterLevel = 23
    GPIO.setup(waterSensor, GPIO.IN)
    
    def waterOn(waterLevel):
        if GPIO.input(waterLevel):
            # print("Water Pump: On")
            GPIO.output(waterPump, GPIO.HIGH)
        