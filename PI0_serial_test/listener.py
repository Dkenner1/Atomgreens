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
    decoder = SerialMsg(ser_in.read())
    while not decoder.msg_complete:
        decoder.interpret(wait_for_byte(ser_in))
    print(decoder.msg)
    eventHub.publish('FLAGS', msg=decoder.msg)
    if decoder.msg['piId'] != piID and ser_out is not None:
        print('Not right device: forwarding out serial out')
        eventHub.publish('DEFAULT', msg=decoder.msg)
        ser_out.write(repackage_bytes(decoder.input_buff))
    else:
        eventHub.publish(decoder.msg['devId'], msg=decoder.msg)
        print('Received New packet')

def baudcalc(ser):
    datagram_rate = ser.baudrate / (ser.bytesize + ser.stopbits + 1)
    return 1 / datagram_rate


