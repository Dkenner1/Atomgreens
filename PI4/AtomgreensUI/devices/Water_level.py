import RPi.GPIO as GPIO
from database.db import connect, add_meas
from database.SQL import PI4_STATUS

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
waterLevel = 16
GPIO.setup(waterLevel, GPIO.IN)

def read_waterLevel(): #read the water level 
    add_meas(1, 14, GPIO.input(waterLevel)) #pi_id, dev_id, value
        
