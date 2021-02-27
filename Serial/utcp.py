from util import *
import struct
import json

class UTCP:
    typeEnum = {'str': 1, 'float': 2, 'int': 0, 'dict': 3}    
    def __init__(self, _ser_out):
        #ser = serial
        self.ser_out = _ser_out
        self.send_packet = None
        self.data_type = None
        self.sendLen = 0
        #dev = devInfo

    def send(self, destpi, destdev, data):
        self.send_packet = None
        self.data_type = typeName(data)
        bdata = self.__data_pack(data)
        self.__header1(destpi, destdev)
        self.__header2(bdata)
        self.sendPacket += bdata
        print('Packet to be sent: ' + str(self.sendPacket))
        self.ser_out.write(self.sendPacket)

    def __header1(self, destpi, destdev):
        dest = chr(bitmask(bitmask(0, destpi, 5, 3), destdev, 2, 3))
        self.sendPacket = struct.pack('c', bytes(dest, encoding='utf8'))

    def __header2(self, bdata):
        head2 = chr(bitmask(bitmask(0, self.typeEnum[self.data_type], 5, 3), len(bdata), shift=0, limit=5))
        self.sendPacket += struct.pack('c', bytes(head2, encoding='utf8'))
             
    def __data_pack(self, data):
        print(data)
        print(self.data_type)
        if self.data_type == 'int':
            return struct.pack('i', data)
        elif self.data_type == 'float':
            return struct.pack('f', data)
        elif self.data_type == 'str':
            strlen = str(len(data))
            return struct.pack(strlen + 's', bytes(data, encoding='utf8'))
        elif self.data_type == 'dict':
            data = json.dumps(data)
            return struct.pack(str(len(data)) + 's', bytes(data, encoding='utf8'))
        else:
            print('error')
            return None



