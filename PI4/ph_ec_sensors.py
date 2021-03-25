import RPi.GPIO as GPIO
from time import sleep
import ADC_callable
import DFRobot_PH
import DFRobot_EC

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

class PH_EC:
    @threaded
    def readPHEC():
        sleep(5)
        waterTemp = ADC_callable.ADC.call(0)

        GPIO.output(13, GPIO.HIGH)
        sleep(1)
        ph = ADC_callable.ADC.call(2)
        GPIO.output(13, GPIO.LOW)

        GPIO.output(15, GPIO.HIGH)
        sleep(1)
        ec = ADC_callable.ADC.call(1)
        GPIO.output(15, GPIO.LOW)

        temperature = (74.4921 / (waterTemp-3.3)) + 70.1467
        PH = DFRobot_PH.DFRobot_PH.readPH(ph)
        EC = DFRobot_EC.DFRobot_PH.readEC(ec, temperature)
        
        add_meas(0, 13, temperature)
        add_meas(0, 11, PH)
        add_meas(0, 12, EC)

        print("Temperature: %.1f ^C EC: %.3f ms/cm PH: %.3f" % (temperature, EC, PH))
