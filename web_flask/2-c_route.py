#!/usr/bin/python3
"""c_route module
Starts a Flask web application
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """hello_hbnb function
    Defines what is return by / route
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """hbnb function
    Defines what is returned by /hbnb route
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """c_route function
    Defines the return value of /c/<text> route
    """
    processed = text.replace('_', ' ')
    return 'C {}'.format(processed)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
