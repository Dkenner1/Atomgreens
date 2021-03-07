import RPi.GPIO as GPIO
from time import sleep
import time
import serial 
import utcp

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
pi_pwm_blue = GPIO.PWM(12,100)
pi_pwm_red = GPIO.PWM(11,100)
blue = 0 
red = 0

class setPWM:
    def PWM_on(red, blue):        
        pi_pwm_red.start(red)
        pi_pwm_blue.start(blue)
        return

    def PWM_off():
        pi_pwm_red.stop()
        pi_pwm_blue.stop()
        return

    def recive(msg):
        PWM_off()
        if (msg > 0):
            if 'red' in msg.keys():
                red = msg['red'] 
            if 'blue' in msg.keys():
                blue = msg['blue'] 
            PWM_on(red, blue)
        return
