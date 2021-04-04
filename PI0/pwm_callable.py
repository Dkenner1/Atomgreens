import RPi.GPIO as GPIO
from time import sleep
import serial 
import utcp

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
pi_pwm_blue = GPIO.PWM(12,100)
pi_pwm_red = GPIO.PWM(11, 1000000)
red=0
blue=0

def PWM_on(red=0, blue=0):        
    pi_pwm_red.start(red)
    pi_pwm_blue.start(blue)

def PWM_off():
    pi_pwm_red.stop()
    pi_pwm_blue.stop()
    

def receive(**kwargs):
    if kwargs is not None:
        msg=kwargs['msg']['msg']
        PWM_off()
        global red, blue
        if 'red' in msg.keys():
            red = msg['red'] 
        if 'blue' in msg.keys():
            blue = msg['blue'] 
        PWM_on(red, blue)
    