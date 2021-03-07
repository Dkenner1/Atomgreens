from util import *
from time import sleep
from unpacker import SerialMsg
import json
import struct
from EventHub import eventHub

config = json.load(open('msg_config.json', 'r'))
piID = config['piID']

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
    print(msg.msg)
    eventHub.publish('FLAGS', msg=msg.msg)
    if msg.msg['piId'] != piID:
        print('Not right device: forwarding out serial out')
        eventHub.publish('DEFAULT', msg=msg.msg)
        ser_out.write(repackage_bytes(msg.input_buff))
    else:
        eventHub.publish(msg.msg['devId'], msg=msg.msg)
        print('Received New packet')

def baudcalc(ser):
    datagram_rate = ser.baudrate / (ser.bytesize + ser.stopbits + 1)
    return 1 / datagram_rate


