import threading

def wait_for_byte(ser_in):
    while not ser_in.inWaiting():
        pass
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