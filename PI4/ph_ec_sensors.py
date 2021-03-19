import RPi.GPIO as GPIO
from time import sleep
import ADC_callable
from DFRobot_PH import readPH
from DFRobot_EC import readEC

GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setwarnings(False) 
class PH_EC:
    def readPHEC():        
        waterTemp = ADC_callable.ADC.call(0)

        GPIO.output(13, GPIO.HIGH)
        ph = ADC_callable.ADC.call(1)
        GPIO.output(13, GPIO.LOW)

        GPIO.output(15, GPIO.HIGH)
        ec = ADC_callable.ADC.call(2)
        GPIO.output(15, GPIO.LOW)

        temperature = (74.4921 / (waterTemp-3.3)) + 70.1467
        PH = ph.readPH(ph, temperature)
        EC = ec.readEC(ec, temperature)

        print("Temperature: %.1f ^C EC: %.2f ms/cm PH: %.2f" % (temperature, EC, PH))

sleep(1.0)