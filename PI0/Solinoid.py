import RPi.GPIO as GPIO
from util import threaded
import serial 
from utcp import UTCP 
ser = serial.Serial(port="/dev/serial0", baudrate=9600)
sender = UTCP(ser)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
solinoid = 31
GPIO.setup(solinoid, GPIO.OUT)
GPIO.output(solinoid, GPIO.LOW)

class solinoid:
    def actuate(command):
        if (command == 1): #if we want to turn on the solinoid 
            GPIO.output(solinoid, GPIO.HIGH)
        else: 
            GPIO.output(solinoid, GPIO.LOW)
    


