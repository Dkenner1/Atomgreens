from flask import Flask
from threading import Thread
from routes.main import main
from server.mongoDB import view_create
import logging, webview
from waitress import serve


app = Flask('Microgreens')
app.register_blueprint(main)


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
    t = Thread(target=start_server)
    t.daemon = True
    t.start()
    width = int(1920 * 0.75)
    height = int(1080 * .75)

    window = webview.create_window('MicrogreensUI', 'http://localhost:5000', width=width,
                                   height=height, )
    webview.start(debug=True)
