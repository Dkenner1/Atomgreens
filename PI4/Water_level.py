import RPi.GPIO as GPIO
from util.db import connect, add_meas
from util.SQL import PI4_STATUS

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
waterLevel = 16
GPIO.setup(waterLevel, GPIO.IN)

class waterLevel:
    def read_waterLevel(): #read the water level 
        add_meas(1, 14, GPIO.input(waterLevel)) #pi_id, dev_id, value
        