import serial
from utcp import UTCP
from listener import listen
from EventHub import eventHub
#from db import add_meas
import json

ser = serial.Serial(port="/dev/serial0", baudrate=9600)  # Open port with baud rate
sender = UTCP(ser)
listen(ser, ser)


def default_msg(msg=None):
    add_meas(msg['piId'], msg['devId'], msg['msg'])

def updatePiID(msg=None):
    if msg['flags'] == 1:
        print('Flag update')
        with open('msg_config.json') as jfile:
            x=json.load(jfile)
            x['piID'] = msg['msg']
        with open('msg_config.json', 'w') as jfile:
            json.dump(x, jfile, indent=4)
            

eventHub.subscribe(updatePiID, "FLAGS")

if __name__ == '__main__':
    sender.send(3, 3, 2, 1)

    
    
