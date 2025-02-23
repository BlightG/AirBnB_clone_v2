#!/usr/bin/python3
''' fetches data from the storage.all() '''
from models import storage
from flask import Flask
from flask import render_template
import jinja2

app = Flask(__name__)
# app.jinja_env.lstrip_blocks = True
# app.jinja_env.trim_blocks = True


@app.route('/states_list', strict_slashes=False)
def states_list():
    ''' returns list of cities '''
    state_list = storage.all('State')
    # print(f'state_list = {state_list.items()}')
    return render_template('7-states_list.html', state_list=state_list)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
