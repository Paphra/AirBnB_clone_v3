#!/usr/bin/python3
"""cities_by_states module
Starts a Flask web application
"""
from flask import Flask, render_template
from models.state import State
from models import storage

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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """python_route function
    Defines the return value of /python/<text> route
    """
    processed = text.replace('_', ' ')
    return 'Python {}'.format(processed)


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """number_route function
    Defines the route of /number/<n>
    Works well if n is a number
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """number_template route
    Defines the return value of /number_template/<int:n>
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """odd_or_even route
    Returns according to the provided number
    """
    state = 'even'
    if n % 2 != 0:
        state = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, state=state)


@app.route('/states_list', strict_slashes=False)
def states_list_route():
    """states_list_route function
    Handles the route /states_list
    """
    states_fetched = storage.all(State)
    states = [state for key, state in states_fetched.items()]
    states = sorted(states, key=lambda x: x['name'])
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """cities_by_states function
    Handles the route above
    """
    from models.state import State
    states = storage.all(State)
    states = [state for key, state in states.items()]
    states = sorted(states, key=lambda x: x['name'])
    for state in states:
        st = State(**state)
        print(st.cities)
        state['cities'] = st.cities
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def do_teardown(app):
    """Close everything
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
