import serial
from utcp import UTCP
from listener import listen

ser = serial.Serial(port="/dev/ttyAMA0", baudrate=9600)  # Open port with baud rate
listen(ser, ser)



