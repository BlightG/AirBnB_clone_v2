#!/usr/bin/python3
''' a script that starts a flask web application '''
from flask import Flask

hbnb = Flask(__name__)


@hbnb.route('/', strict_slashes=False)
def home():
    ''' returns when / is typed '''
    return "Hello HBNB"


@hbnb.route('/hbnb', strict_slashes=False)
def HBNB():
    ''' returns when /hbnb is typed '''
    return "HBNB"

if __name__ == '__main__':
    hbnb.run(host="0.0.0.0", port=5000)
