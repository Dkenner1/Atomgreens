import RPi.GPIO as GPIO
from time import sleep
import ADC_callable
import DFRobot_PH
#import DFRobot_EC

GPIO.setup(13, GPIO.OUT)
#GPIO.setup(15, GPIO.OUT)
GPIO.setwarnings(False)


class PH_Calibration:
	def readPHTest():
		waterTemp = 25

		GPIO.output(13, GPIO.HIGH)
		ph = ADC_callable.ADC.call(1)
		GPIO.output(13, GPIO.LOW)

		#GPIO.output(15, GPIO.HIGH)
		#ec = ADC_callable.ADC.call(2)
		#GPIO.output(15, GPIO.LOW)

		temperature = (74.4921 / (waterTemp - 3.3)) + 70.1467
		temperature = 25
		PH = DFRobot_PH.ph.calibration(ph, temperature)
		#EC = ec.DFRobot_EC.calibration(ec, temperature)

		print("PH: %.2f" % (PH))


sleep(1.0)