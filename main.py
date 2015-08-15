#!/usr/bin/env python

from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)


@app.route('/hello/')
def hello_world():
    return 'Hello World!'

@app.route("/")
def main():
    return render_template('radar.html')

if __name__ == '__main__':
    app.run(host='192.168.0.101', port=8000,debug=True)