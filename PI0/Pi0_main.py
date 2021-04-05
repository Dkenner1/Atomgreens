import RPi.GPIO as GPIO
from time import sleep
import serial
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

from EventHub import eventHub
from listener import listen
from behaviors import *
GPIO.setup(32,GPIO.OUT) #turns on blue lights
GPIO.output(32, GPIO.HIGH)
import  pwm_callable

# from weight_sensor import w_sensor
#import Temp_and_humidity_sensor_pi0
import Solinoid
from utcp import UTCP
pwm_callable.PWM_on()
ser = serial.Serial(port="/dev/serial0", baudrate=9600)  # Open port with baud rate
listen(ser, ser)
sender = UTCP(ser)
def tempfunc(**kwargs):
	sender.send(1,4, 5)

eventHub.subscribe(updatePiID, 'FLAGS')
eventHub.subscribe(fwd, 'FWD')
eventHub.subscribe(tempfunc, 2)
#eventHub.subscribe(Temp_and_humidity_sensor_pi0.TH.read_temp_humidity, 3)
#eventHub.subscribe(Temp_and_humidity_sensor_pi0.TH.read_temp_humidity, 4)
# eventHub.subscribe(w_sensor.weight, 3)
eventHub.subscribe(Solinoid.actuate, 4)
eventHub.subscribe(pwm_callable.receive, 5, 6)

