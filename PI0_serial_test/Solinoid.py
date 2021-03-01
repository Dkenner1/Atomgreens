import RPi.GPIO as GPIO
from time import sleep
import time
import serial 
import utcp

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(31,GPIO.OUT) #sets watering actuator as output
GPIO.output(31, GPIO.LOW) #turn off the device 

class setPWM:
    def recive(msg):
        if (msg == 0):
            GPIO.output(31, GPIO.LOW) #turn off the device 
        elif (msg == 1):
            GPIO.output(31, GPIO.HIGH) #turn on the device 
        else:
            #handle error
            sender.send(0, 4, {"Error": 1}) #PI id, Sensor ID, data
        return

pwm = setPWM()