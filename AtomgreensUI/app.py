from flask import Flask
from routes.main import main
import logging
from waitress import serve


app = Flask('Atomgreens')
app.register_blueprint(main)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

def start_server():
    print('~ ' * 5)
    print('in start_server')
    app.logger.setLevel(logging.INFO)
    serve(app, host='0.0.0.0', port=5000)
    #app.run(host='0.0.0.0', port=5000, threaded=True)


def start_db():
    print('~ ' * 5)
    print('in start_server')
    app.logger.setLevel(logging.INFO)
    app.run(host='localhost', port=1111, threaded=True)


if __name__ == '__main__':
    start_server()

