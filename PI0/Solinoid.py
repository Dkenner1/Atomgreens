import RPi.GPIO as GPIO
from util import threaded
import serial 
from utcp import UTCP 
ser = serial.Serial(port="/dev/serial0", baudrate=9600)
sender = UTCP(ser)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

class solinoid:
    def Open():
        
        return 


