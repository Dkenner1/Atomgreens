import serial
from serial.utcp import UTCP
try:
    ser = serial.Serial(port="/dev/serial0", baudrate=9600)  # Open port with baud rate
    sender = UTCP(ser)
except:
    print("unable to open serial object")

config={
  "beets": {
    "red": 70,
    "blue": 30,
    "ph turns": 10,
    "ec turns": 10,
    "runTime": 604800
  },
  "brocolli": {
    "red": 50,
    "blue": 50,
    "ph turns": 10,
    "ec turns": 10,
    "runTime": 604800
  }
}

def tray_start(trayid, microgreen):
    sel = config[microgreen]
    red = sel['red']
    blue = sel['blue']
    ec = sel['ec turns']
    ph = sel['ph turns']

    sender.send(trayid, 5, red)
    sender.send(trayid, 6, blue)
    sender.send(trayid, 9, ph)
    sender.send(trayid, 10, ec)

def tray_stop(trayid):
    ser = serial.Serial(port="/dev/serial0", baudrate=9600)  # Open port with baud rate
    sender = UTCP(ser)
    sender.send(trayid, 5, 0)
    sender.send(trayid, 6, 0)
    sender.send(trayid, 9, 0)
    sender.send(trayid, 10, 0)