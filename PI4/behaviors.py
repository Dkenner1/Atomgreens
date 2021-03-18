from database.db import add_meas

def store(**kwargs):
    msg=kwargs['msg']
    add_meas(msg['piId'], msg['devId'], msg['msg'])