import RPi.GPIO as GPIO
from time import sleep
import ADC_callable
import DFRobot_PH
#import DFRobot_EC

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(13, GPIO.OUT)

waterTemp = 25

GPIO.output(13, GPIO.HIGH)
sleep(1)
ph = ADC_callable.ADC.call(2)
GPIO.output(13, GPIO.LOW)

temperature = (74.4921 / (waterTemp - 3.3)) + 70.1467
temperature = 25
PH = DFRobot_PH.DFRobot_PH.calibration(ph)

print(ph)