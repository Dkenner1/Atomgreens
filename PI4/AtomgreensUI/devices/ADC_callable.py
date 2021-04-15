from time import sleep
import time
import spidev
import RPi.GPIO as GPIO
spi = spidev.SpiDev()

def call(line):
    spi.open(0, 0) #pi channel for pins 19,21,23,24,26; & CE0(24) used instead of CE1(26)
    spi.max_speed_hz = 1500000 # Set max speed of communication

    #Water temp: line = 0
    #EC: line = 1
    #PH: line = 2
    line = (line+5)<<3
    MSG1 = spi.xfer2([line, 0x00])
    MSG2 = spi.xfer2([line, 0x00])
    MSG3 = spi.xfer2([line, 0x00])

    answer = [0,0] #assignment before referance
    answer[0] = round((MSG1[0]+MSG2[0]+MSG3[0])/3) #average 3 results for better accuracy
    answer[1] = round((MSG1[1]+MSG2[1]+MSG3[1])/3) #average 3 results for better accuracy

    A = answer[0]<<6
    B = answer[1]>>2
    answer = ((A+B)/1024)*3.3 #calculate voltage from abstract

    formatted_string = "{:.3f}".format(answer) #truncate float
    answer = float(formatted_string)
    spi.close()
    return answer



