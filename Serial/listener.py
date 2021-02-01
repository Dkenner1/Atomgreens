from util import *
from time import sleep
from definitions import piID
import serial, struct


@threaded
def listen(ser_in, ser_out):
    sleepamt = baudcalc(ser_in)
    print('listening')
    while True:
        if ser_in.inWaiting():
            read_msg(ser_in, ser_out)
            print('Read message, blocking again')
        sleep(sleepamt)


def wait_for_byte(ser_in):
    while not ser_in.inWaiting():
        pass
    return ser_in.read()


def read_msg(ser_in, ser_out):
    piID = 1
    recv_buff = []
    recv_buff += ser_in.read()

    dest = bit_seg_read(recv_buff[-1], 5, 7)
    dev = bit_seg_read(recv_buff[-1], 2, 4)
    flgs = bit_seg_read(recv_buff[-1], 2, 4)

    recv_buff += wait_for_byte(ser_in)
    typ = bit_seg_read(recv_buff[-1], 5, 7)
    msglen = bit_seg_read(recv_buff[-1], 0, 4)
    
    for byt in range(1, msglen):
        recv_buff += wait_for_byte(ser_in)
        print(recv_buff)
    print('~' * 5)
    print(recv_buff)
    print(repackage_bytes(recv_buff))
    if dest != piID:
        ser_out.write(repackage_bytes(recv_buff))
    else:
        print('Received New packet')


def repackage_bytes(chr_arr):
    bstr = bytes()
    for byt in chr_arr:
        bstr += struct.pack('c', bytes(chr(byt), encoding='utf8'))
    return bstr


def bit_seg_read(bitstr, frm, to):
    if frm > to:
        print('error: frm must be smaller than to')
        return None
    mask = 2 ** (to - frm + 1) - 1
    bitstr &= mask << frm
    return bitstr >> frm


def baudcalc(ser):
    datagram_rate = ser.baudrate / (ser.bytesize + ser.stopbits + 1)
    return 1 / datagram_rate
