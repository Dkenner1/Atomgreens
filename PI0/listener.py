from util import *
from time import sleep
from unpacker import SerialMsg
import json
import struct
from EventHub import eventHub

config = json.load(open('config.json', 'r'))

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
    global config
    sleepamt = baudcalc(ser_in)
    msg = SerialMsg(ser_in.read())
    while not msg.msg_complete:
        try:
            msg.interpret(wait_for_byte(ser_in, sleepamt))
        except RuntimeError as err:
            print("Error: ", err)
            return
    print("Received msg: " + str(msg.msg))
    if msg.msg['flags']:
        eventHub.publish('FLAGS', ser=ser_out, msg=msg.msg)
        config = json.load(open('config.json', 'r'))
    elif msg.msg['piId'] != config['piID']:
        eventHub.publish('DEFAULT', 'FWD', ser=ser_out, msg=msg.msg, repackaged=repackage_bytes(msg.input_buff))
    else:
        eventHub.publish(msg.msg['devId'], msg=msg.msg)

def baudcalc(ser):
    datagram_rate = ser.baudrate / (ser.bytesize + ser.stopbits + 1)
    return 1 / datagram_rate


