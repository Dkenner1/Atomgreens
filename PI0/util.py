import threading
from time import sleep

config={
    "piID": 1,
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

def wait_for_byte(ser_in, sleepamt):
    timeout=0
    while not ser_in.inWaiting():
        timeout += 1
        if timeout > 5:
            raise RuntimeError("Message Timeout")
        sleep(sleepamt)
    return ser_in.read()

def bitmask(src=0, mod=0, shift=0, limit=None):
    if limit is not None:
        mask = (2 ** limit) - 1
        mod &= mask
    return src | (mod << shift)

def bit_seg_read(bitstr, frm, to):
    if frm > to:
        print('error: frm must be smaller than to')
        return None
    mask = 2 ** (to - frm + 1) - 1
    bitstr &= mask << frm
    return bitstr >> frm


def typeName(val):
    return type(val).__name__


def threaded(func):
    def threadedfunc(*args, **kwargs):
        thrd = threading.Thread(target=func, args=args, kwargs=kwargs)
        thrd.start()
    return threadedfunc


def intarr2str(buff):
    s=""
    for i in buff:
        s += chr(i)
    return s

def repackage_bytes(chr_arr):
    bstr = bytes()
    for byt in chr_arr:
        bstr += byt.to_bytes(1, 'big')
    return bstr
