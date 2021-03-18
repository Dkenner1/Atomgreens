import RPi.GPIO as GPIO
from time import sleep
import serial
from utcp import UTCP 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
waterLevel = 16
GPIO.setup(waterLevel, GPIO.IN)

ser = serial.Serial(port="/dev/serial0", baudrate=9600)
sender = UTCP(ser)

class TH:
    def read_temp_humidity(): #get a temp measurment
        add_meas(1, 14, GPIO.input(waterLevel)) #pi id, dev id, value
        return