import RPi.GPIO as GPIO
GPIO.setwarnings(False)
from time import sleep
import serial
from utcp import UTCP
from database.db import connect, add_meas
from database.SQL import PI4_STATUS

import smbus
from smbus import SMBus
from smbus2 import SMBus, i2c_msg

bus = SMBus(1)
i2c_ch = 1 
i2c_address = 64 #HDC1080 address on the I2C bus

reg_Temperature = 0x00    #Temperature measurement output
reg_Humidity = 0x01       #Relative Humidity measurement output
reg_Configuration = 0x02  #HDC1080 configuration and status
reg_Serial_ID1 = 0xFB     #First 2 bytes of the serial ID of the part
reg_Serial_ID2 = 0xFC     #Mid 2 bytes of the serial ID of the part
reg_Serial_ID3 = 0xFD     #Last byte bit of the serial ID of the part
reg_Manufacturer_ID = 0xFE#ID of Texas Instruments
reg_Device_ID = 0xFF      #ID of the device

def read_temp_humidity(): #get a temp measurment     
    #register_config = [0x10,0x00]
    #bus.write_i2c_block_data(i2c_address, reg_Configuration, register_config) #update the resister configuration 
    msg = i2c_msg.write(i2c_address,[reg_Temperature])
    bus.i2c_rdwr(msg)
    sleep(.02)
    msg = i2c_msg.read(i2c_address,4)
    bus.i2c_rdwr(msg)
    test =list(msg)
    print (test)

    temp = (test[0]<<8)^test[1]
    tempurature = (temp/pow(2,16))*165-40
    formatted_string = "{:.1f}".format(tempurature)
    tempurature = float(formatted_string)
    print (tempurature)
    add_meas(0, 2, tempurature)

    hum = (test[2]<<8)^test[3]
    humidity = (hum/pow(2,16))*100
    formatted_string = "{:.1f}".format(humidity)
    humidity = float(formatted_string)
    add_meas(0, 1, humidity)
    print (humidity)

    return
