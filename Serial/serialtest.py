import serial
from utcp import UTCP
from listener import listen

ser = serial.Serial(port="/dev/serial0", baudrate=9600)  # Open port with baud rate
sender = UTCP(ser)
listen(ser, ser)

if __name__ == '__main__':
    sender.send(1, 3, 16)


