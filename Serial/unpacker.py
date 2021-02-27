from util import bit_seg_read, intarr2str
import struct
import json

msg_config = json.load(open('msg_config.json', 'r'))


class SerialMsg:
    def __init__(self, initialbyte, _config=msg_config):
        self.input_buff = []
        self.config = _config
        self.details = self.config['details']
        self.type_enum = self.config['type_enum']
        self.curr_byte = 1
        self.msg = self.create_msg_pattern()
        self.msg_complete = False
        self.repacked = None
        self.interpret(initialbyte)

    def interpret(self, dbyte):
        if self.msg_complete:
            return

        self.input_buff += dbyte
        if self.curr_byte <= self.config['headers']:
            for key, val in self.details.items():
                if val['byte'] == self.curr_byte:
                    self.msg[key] = bit_seg_read(self.input_buff[-1], val['rng'][0], val['rng'][1])
            self.curr_byte += 1
            return

        self.msg['raw_msg'] += (dbyte)
        if self.curr_byte == self.msg['length'] + self.config['headers']:
            self.convert_data()
            self.msg_complete=True
            self.repack()

        self.curr_byte += 1

    def repack(self):
        if self.msg['type'] == self.type_enum['int']:
            self.repacked = struct.pack('i', self.msg['msg'])
        elif self.msg['type'] == self.type_enum['float']:
            self.repacked = struct.pack('f', self.msg['msg'])
        elif self.msg['type'] == self.type_enum['str']:
            self.repacked = struct.pack(str(self.msg['length']) + 's', bytes(self.msg['msg'], encoding='utf8'))
        else:
            self.msg['raw_msg']
            print('Repacking error')
            return None

    def create_msg_pattern(self):
        msgdict = {'raw_msg': [], 'msg': None}
        headerinfo = {key: None for key in self.config['details'].keys()}
        return {**msgdict, **headerinfo}

    def convert_data(self):
        print(self.msg['raw_msg'])
        if self.msg['type'] == self.type_enum['int']:
            self.msg['msg'] = struct.unpack('i', bytearray(self.msg['raw_msg']))[0]
        elif self.msg['type'] == self.type_enum['float']:
            self.msg['msg'] = struct.unpack('f', bytearray(self.msg['raw_msg']))[0]
        elif self.msg['type'] == self.type_enum['str']:
            self.msg['msg'] = intarr2str(self.msg['raw_msg'])
        elif self.msg['type'] == self.type_enum['dict']:
            self.msg['msg'] = json.loads(intarr2str(self.msg['raw_msg']))
        else:
            print('Conversion error')
