import RPi.GPIO as GPIO
from time import sleep
import ADC_callable
import DFRobot_PH
import DFRobot_EC

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(15, GPIO.OUT)

temperature = 22.5

GPIO.output(15, GPIO.HIGH)
sleep(1)
EC = ADC_callable.ADC.call(1)
GPIO.output(15, GPIO.LOW)
print(EC)

_kvalue                 = .987
_kvalueLow              = 1.0728
_kvalueHigh             = 1.0687
_cmdReceivedBufferIndex = 0
_voltage                = 0.0
_temperature            = 25.0


rawEC = 1000*EC/820.0/200.0
print(rawEC)
if (rawEC>0.0009 and rawEC<.0019): 
    compECsolution = 1.413*(1.0+0.0185*(temperature-25.0))
    KValueLow = 820.0*200.0*compECsolution/1000000.0/EC
    print(KValueLow)
elif (rawEC>.009 and rawEC<.0168):
    compECsolution = 12.88*(1.0+0.0185*(temperature-25.0))
    KValueHigh = 820.0*200.0*compECsolution/1000000.0/EC
    print(KValueHigh)


