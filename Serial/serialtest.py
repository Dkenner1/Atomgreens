import serial
from utcp import UTCP
from listener import listen
from EventHub import eventHub
from definitions import piID

ser = serial.Serial(port="/dev/serial0", baudrate=9600)  # Open port with baud rate
sender = UTCP(ser)
listen(ser, ser)


def foo(msg):
    print("You've got mail! *** " + str(msg))


eventHub.subscribe(foo, "DEFAULT")

def test():
    sender.send(2, 3, {"hello!": 1})

    
    
