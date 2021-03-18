import json
from utcp import UTCP
def fwd(**kwargs):
    print('Not right device: forwarding out serial out')
    kwargs['ser'].write(kwargs['repackaged'])

def updatePiID(**kwargs):
    msg = kwargs['msg']
    if msg['flags'] == 1:
        print('Flag update')
        with open('config.json') as jfile:
            x=json.load(jfile)
            x['piID'] = msg['msg']+1
        with open('config.json', 'w') as jfile:
            json.dump(x, jfile, indent=4)
        sender = UTCP(kwargs['ser'])
        sender.send(0,0, msg['msg']+1, 1)
