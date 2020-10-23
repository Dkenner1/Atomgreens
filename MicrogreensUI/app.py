from flask import Flask, render_template, redirect, request, url_for
from threading import Thread, Lock, Event
from pages.main import main

import logging, os, shelve, webview, sys, traceback

app = Flask('Microgreens')
app.register_blueprint(main)


def start_server():
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
    window = webview.create_window('Microgreens', 'http://localhost:1111/', width=width,
                                   height=height, )
    webview.start(gui="qt", debug=True)