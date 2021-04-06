import RPi.GPIO as GPIO
from time import sleep
import serial
import utcp

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
pi_pwm_blue = GPIO.PWM(32,100)
pi_pwm_red = GPIO.PWM(33,100)
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
        msg=kwargs['msg']
        print("receive pwm msg: " + str(msg))
        if msg['devId']==5:
            if msg['msg'] != 0:
                pi_pwm_red.start(msg['msg'])
            else:
                pi_pwm_red.stop()
        if msg['devId']==6:
            if msg['msg'] != 0:
                pi_pwm_blue.start(msg['msg'])
            else:
                pi_pwm_blue.stop()


