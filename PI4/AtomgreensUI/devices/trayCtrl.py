import serial
from serial.utcp import UTCP
from database.db import new_run
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
    "runTime": 864000
  },
  "broccoli": {
    "red": 50,
    "blue": 50,
    "ph turns": 10,
    "ec turns": 10,
    "runTime": 604800
  }
}

def tray_start(trayid, microgreen):
    sel = config[microgreen]
    new_run(trayid, microgreen, sel['runTime'])