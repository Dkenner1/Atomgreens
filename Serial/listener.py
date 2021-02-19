from util import *
from time import sleep
from unpacker import SerialMsg
from definitions import piID
import struct


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
    if msg.msg['piId'] != piID:
        print('Not right device: forwarding out serial out')
        ser_out.write(repackage_bytes(msg.input_buff))
    else:
        print('Received New packet')


def repackage_bytes(chr_arr):
    bstr = bytes()
    for byt in chr_arr:
        bstr += struct.pack('c', bytes(chr(byt), encoding='utf8'))
    return bstr


def baudcalc(ser):
    datagram_rate = ser.baudrate / (ser.bytesize + ser.stopbits + 1)
    return 1 / datagram_rate


