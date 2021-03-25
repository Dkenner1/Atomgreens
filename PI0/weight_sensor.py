import RPi.GPIO as GPIO
from time import sleep
from statistics import mean
from util import threaded
import serial 
from utcp import UTCP 
ser = serial.Serial(port="/dev/serial0", baudrate=9600)
sender = UTCP(ser)

class passweight:
    @threaded
    def weight(msg=None):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        power = 11
        CLK = 13
        DO = 15
        count = 0
        count_total = []
        count_ave = 0
        ratio = -20.5
        offset = 8286827.2
        GPIO.setup(power,GPIO.OUT) #sets pin 11 to be an output
        GPIO.setup(CLK,GPIO.OUT) #sets pin 13 to be an output
        GPIO.setup(DO,GPIO.IN, pull_up_down=GPIO.PUD_UP) #sets pin 15 to be an output with pull up control

        j = 5
        while (j != 0):
            GPIO.output(power, GPIO.HIGH) #turn on the device 
            GPIO.output(CLK, GPIO.LOW) #keep the clock low until the DO turns low
            i = 24
            while (GPIO.input(DO)!= 1):#detect when the weight sensor starts to transmit
                count = count + 1
            count = 0
            while (i != 0):
                GPIO.output(CLK, GPIO.HIGH) #put the CLK high to start reading bits
                count = count*2 #shift the bits to the left by 1
                GPIO.output(CLK, GPIO.LOW) #put the CLK low to start the next cycle
                if (GPIO.input(DO) == 1): #if the weight sensor 
                    count = count + 1
                    print('1')
                else:
                    print('0')
                i = i-1
            GPIO.output(CLK, GPIO.HIGH) #put the clock high for one lasting setting of the gain 
            count = count^0x800000
            GPIO.output(CLK, GPIO.LOW) #put the clock low and wait for the next reading
            if(count >= 8260000 and count <= 8290000):
                count_total.append(count)
            else:
                j = j + 1
            count = 0
            j = j-1

        count_ave = mean(count_total)
        count_ave = (count_ave - offset)/ratio
        sender.send(0, 3, int(count_ave))
        return 



