"""
Pitt MakerSpace Control Panel Web Interface.
"""
import datetime
from flask import Flask, render_template, redirect, url_for, request
from csv_helper import read_csv


# DATABASE SETUP
CSV_FILE = 'ms_lockout.csv'
DATA = read_csv(CSV_FILE)
USER_IDS = [col[0] for col in DATA]
access_col_idx = 3


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/control')
def control():
    return render_template('control.html')


@app.route('/usage')
def usage():
    return render_template('usage.html')


@app.route('/post', methods=['POST'])
def get_post():
    device, uid = request.form['device'], request.form['uid']
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M")
    message = 'Time: %s | Device: %s | UID: %s' % (time, device, uid)
    print(message)

    try:
        user_index = USER_IDS.index(uid)
        print('User found: %i' % user_index)
        if DATA[user_index][access_col_idx] == 'yes':
            print('%s has acess.' % DATA[user_index][1])
            response = 'yes'
        else:
            print('%s does not have acess.' % DATA[user_index][1])
            response = 'no'
    except:
        print('User not found!')
        response = 'not-found'

    return response


# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('/'))
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
