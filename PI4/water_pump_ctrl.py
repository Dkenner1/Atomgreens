import RPi.GPIO as GPIO
from time import sleep
from database.db import connect, add_meas
from database.SQL import PI4_STATUS
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# GPIO pin for water pump
waterPump = 18
GPIO.setup(waterPump, GPIO.OUT)

# GPIO pin for air pump
airPump = 22
GPIO.setup(airPump, GPIO.OUT)

# GPIO pin for water level sensor
waterLevel = 16
GPIO.setup(waterLevel, GPIO.IN)

def water(ctrl):
    if (ctrl): # and GPIO.input(waterLevel)!=0
        print(GPIO.input(waterLevel)) #should print 1
        # print("Water Pump: On")
        GPIO.output(waterPump, GPIO.HIGH)
        GPIO.output(airPump, GPIO.HIGH)
        add_meas(1, 14, GPIO.input(waterLevel)) #tell the database that the water level is okay 
    elif (ctrl == 0): #if the user says to turn off the pump
        GPIO.output(waterPump, GPIO.LOW)
        GPIO.output(airPump, GPIO.LOW)
        add_meas(1, 14, GPIO.input(waterLevel)) #pi id, dev id, value
    else: #if the water level is too low to turn on the pump
        print('water level low')
        GPIO.output(waterPump, GPIO.LOW)
        GPIO.output(airPump, GPIO.LOW)
        add_meas(1, 14, GPIO.input(waterLevel)) #pi id, dev id, value
        
        
            
            