from util import *
from time import sleep
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
    recv_buff = []
    recv_buff += ser_in.read()

    dest = bit_seg_read(recv_buff[-1], 5, 7)
    dev = bit_seg_read(recv_buff[-1], 2, 4)
    flgs = bit_seg_read(recv_buff[-1], 2, 4)

    recv_buff += wait_for_byte(ser_in)
    typ = bit_seg_read(recv_buff[-1], 5, 7)
    msglen = bit_seg_read(recv_buff[-1], 0, 4)

    for byt in range(0, msglen):
        recv_buff += wait_for_byte(ser_in)
        print(recv_buff)
    print('~' * 5)
    print(recv_buff)
    print(repackage_bytes(recv_buff))
    print('Pi ID is: ' + str(piID))
    if dest != piID:
        print('Not right device: forwarding out serial out')
        ser_out.write(repackage_bytes(recv_buff))
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


