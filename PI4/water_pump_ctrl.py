import RPi.GPIO as GPIO
from time import sleep
#from util.db import connect, add_meas
#from util.SQL import PI4_STATUS

class WaterPumpCtrl:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    # GPIO pin for water pump
    waterPump = 18
    GPIO.setup(waterPump, GPIO.OUT)

    # GPIO pin for water pump
    waterPump = 18
    GPIO.setup(waterPump, GPIO.OUT)
    
    # GPIO pin for water level sensor
    waterLevel = 16
    GPIO.setup(waterLevel, GPIO.IN)

    def water(waterPump):
        if (waterPump and GPIO.input(waterLevel)):
            # print("Water Pump: On")add_meas(1, 9, (pumpCnt + ecPumpCount))
            GPIO.output(waterPump, GPIO.HIGH)
            
            add_meas(1, 14, GPIO.input(waterLevel)) #tell the database that the water level is okay 
        elif (waterPump == 0): #if the user says to turn off the pump
            GPIO.output(waterPump, GPIO.LOW) 
            add_meas(1, 14, GPIO.input(waterLevel)) #pi id, dev id, value
        else: #if the water level is too low to turn on the pump
            GPIO.output(waterPump, GPIO.LOW)
            add_meas(1, 14, GPIO.input(waterLevel)) #pi id, dev id, value
            
            
            
            