import RPi.GPIO as GPIO
from time import sleep
import ADC_callable
import DFRobot_PH
import DFRobot_EC

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(15, GPIO.OUT)

waterTemp = 25

GPIO.output(15, GPIO.HIGH)
sleep(1)
EC = ADC_callable.ADC.call(1)
GPIO.output(15, GPIO.LOW)

temperature = (74.4921 / (waterTemp - 3.3)) + 70.1467
temperature = 25
EC = DFRobot_EC.DFRobot_EC.calibration(EC, temperature)

print(EC)