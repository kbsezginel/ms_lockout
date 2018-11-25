"""
Pitt MakerSpace Control Panel Web Interface.
"""
import datetime
from flask import Flask, render_template, redirect, url_for, request


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
    device, status = request.form['device'], request.form['status']
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M")
    message = 'Time: %s | Device: %s | Status: %s' % (time, device, status)
    print(message)
    return message


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
