from database.db import add_meas

def store(**kwargs):
<<<<<<< HEAD
    msg=kwargs['msg']
    add_meas(msg['piId'], msg['devId'], msg['msg'])
=======
	msg=kwargs['msg']
	add_meas(msg['piId'], msg['devId'], msg['msg'])
>>>>>>> 086e41db819db4496e28a700495500e7c58da1ff
