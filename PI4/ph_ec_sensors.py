import RPi.GPIO as GPIO
from time import sleep
from database.db import add_meas
import ADC_callable
import DFRobot_PH
import DFRobot_EC
from util import threaded 

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
#@threaded
def readPHEC():
    ADC_callable.call(0)
    sleep(5)
    waterTemp = ADC_callable.call(0)
    
    GPIO.output(13, GPIO.HIGH)
    ADC_callable.call(2)
    sleep(5)
    ph = ADC_callable.call(2)
    GPIO.output(13, GPIO.LOW)
    
    GPIO.output(15, GPIO.HIGH)
    ADC_callable.call(1)
    sleep(5)
    ec = ADC_callable.call(1)
    GPIO.output(15, GPIO.LOW)
    
    temperature = (74.4921 / (waterTemp-3.3)) + 70.1467
    PH = DFRobot_PH.readPH(ph)
    EC = DFRobot_EC.readEC(ec, temperature)
    
    add_meas(0, 13, temperature)
    PH = 5.5
    add_meas(0, 11, PH)
    add_meas(0, 12, EC)

    print("Temperature: %.1f ^C EC: %.3f ppm PH: %.3f" % (temperature, EC, PH))

