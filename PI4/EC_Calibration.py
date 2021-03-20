import RPi.GPIO as GPIO
from time import sleep
import ADC_callable
import DFRobot_PH
import DFRobot_EC

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(15, GPIO.OUT)

temperature = 22.3

GPIO.output(15, GPIO.HIGH)
sleep(1)
EC = ADC_callable.ADC.call(1)
GPIO.output(15, GPIO.LOW)
print(EC)

rawEC = (1000*EC/820.0)/200.0
print(rawEC)
if (rawEC>0.9 and rawEC<1.9): 
    compECsolution = 12.88*(1.0+0.0185*(temperature-25.0))
    KValueLow = 820.0*200.0*compECsolution/1000.0/EC
    print(KValueLow)
elif (rawEC>9 and rawEC<16.8):
    compECsolution = 12.88*(1.0+0.0185*(temperature-25.0))
    KValueHigh = 820.0*200.0*compECsolution/1000.0/EC
    print(KValueHigh)


