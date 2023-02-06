#!/usr/bin/python3
''' a script that starts a flask web application '''
from flask import Flask
from flask import render_template

hbnb = Flask(__name__)


@hbnb.route('/', strict_slashes=False)
def home():
    ''' returns when / is typed '''
    return "Hello HBNB"


@hbnb.route('/hbnb', strict_slashes=False)
def HBNB():
    ''' returns when /hbnb is typed '''
    return "HBNB"


@hbnb.route('/c/<string:text>', strict_slashes=False)
def C_is_fun(text):
    ''' return c followed by user inserted text '''
    escaped_text = text.replace('_', ' ')
    return "C %s" % escaped_text


@hbnb.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@hbnb.route('/python/<string:text>', strict_slashes=False)
def python_is_cool(text):
    ''' return python followed by user inserted text or default text'''
    escaped_text = text.replace('_', ' ')
    return "Python %s" % escaped_text


@hbnb.route('/number/<int:n>', strict_slashes=False)
def number(n):
    ''' checks if url has int or not '''
    if isinstance(n, int):
        return "%d is a number" % n


@hbnb.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    ''' checks if url has int or not '''
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


if __name__ == '__main__':
    hbnb.run(host="0.0.0.0", port=5000)
