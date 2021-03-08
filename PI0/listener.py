from util import *
from time import sleep
from unpacker import SerialMsg
#import json
import struct
from EventHub import eventHub

config = {
    "piID": 4,
    "headers": 2,
    "details": {
        "piId": {
            "byte": 1,
            "rng": [
                5,
                7
            ]
        },
        "devId": {
            "byte": 1,
            "rng": [
                2,
                4
            ]
        },
        "flags": {
            "byte": 1,
            "rng": [
                0,
                1
            ]
        },
        "type": {
            "byte": 2,
            "rng": [
                5,
                7
            ]
        },
        "length": {
            "byte": 2,
            "rng": [
                0,
                4
            ]
        }
    },
    "type_enum": {
        "int": 0,
        "str": 1,
        "float": 2,
        "dict": 3
    }
}
piID = 1

@threaded
def listen(ser_in, ser_out):
    sleepamt = baudcalc(ser_in)
    print('listening')
    while True:
        if ser_in.inWaiting():
            print('New Message')
            read_msg(ser_in, ser_out)
            print('Read message, blocking again')
        sleep(sleepamt)


def read_msg(ser_in, ser_out):
    msg = SerialMsg(ser_in.read())
    while not msg.msg_complete:
        msg.interpret(wait_for_byte(ser_in))
    print("Received msg: " + str(msg.msg))
    if msg.msg['piId'] != piID:
        print('Not right device: forwarding out serial out')
        eventHub.publish('DEFAULT', msg=msg.msg)
        ser_out.write(repackage_bytes(msg.input_buff))
    else:
        eventHub.publish(msg.msg['devId'], 'FLAGS', msg=msg.msg)

def baudcalc(ser):
    datagram_rate = ser.baudrate / (ser.bytesize + ser.stopbits + 1)
    return 1 / datagram_rate


