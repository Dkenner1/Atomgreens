from flask import Flask
from routes import main, service
import logging, threading
from waitress import serve

app = Flask('Atomgreens')
app.register_blueprint(main.main)
app.register_blueprint(service.service_routes)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

def start_server():
    print('~ ' * 5)
    print('in start_server')
    app.logger.setLevel(logging.INFO)
    serve(app, host='0.0.0.0', port=5000)
    #app.run(host='0.0.0.0', port=5000, threaded=True)



if __name__ == '__main__':
    start_server()

