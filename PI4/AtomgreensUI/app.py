from flask import Flask
from routes import main, service
from util.util import threaded
import logging
from waitress import serve
from database.db import connect
import time
from devices.trayCtrl import tray_stop
from database.SQL import SELECT_EXPIRED_RUNS
app = Flask('Atomgreens')
app.register_blueprint(main.main)
app.register_blueprint(service.service_routes)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

@threaded
def start_server():
    print('~ ' * 5)
    print('in start_server')
    app.logger.setLevel(logging.INFO)
    serve(app, host='0.0.0.0', port=5000)
    #app.run(host='0.0.0.0', port=5000, threaded=True)

if __name__ == '__main__':
    start_server()
    while(True):
        t = time.time()
        conn = connect()
        cur = conn.cursor()
        for run in cur.execute(SELECT_EXPIRED_RUNS, (int(time.time()))):
            tray_stop(1)
        time.sleep(1)




