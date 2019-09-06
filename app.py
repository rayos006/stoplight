from flask import Flask, render_template, request
import json
import stoplight
from time import sleep
import threading

# Global Variables
global STOP
global STATUS
STATUS = 'off'

# Flask Declarations
app = Flask(__name__)
application = app


@app.route('/')
def home():
    """
    This function returns the home page
    """
    global STATUS
    STATUS = "off"
    # TODO Set led to off
    return render_template('index.html')


@app.route('/off')
def off():
    """
    This function returns the off page
    """
    if 't' in globals():
        cycle_stop()
        t.join()
    global STATUS
    STATUS = 'off'
    stoplight.off()
    return render_template('index.html')


@app.route('/red')
def red():
    """
    This function returns the red page
    """
    if 't' in globals():
        cycle_stop()
        t.join()
    global STATUS
    STATUS = 'red'
    stoplight.red()
    return render_template('index.html')


@app.route('/yellow')
def yellow():
    """
    This function returns the yellow page
    """
    if 't' in globals():
        cycle_stop()
        t.join()
    global STATUS
    STATUS = 'yellow'
    stoplight.yellow()
    return render_template('index.html')


@app.route('/green')
def green():
    """
    This function returns the green page
    """
    if 't' in globals():
        cycle_stop()
        t.join()
    global STATUS
    STATUS = 'green'
    stoplight.green()
    return render_template('index.html')


@app.route('/run')
def run():
    """
    This function returns the run page
    """
    global t
    t = threading.Thread(target=cycle_run)
    t.start()
    return render_template('index.html')


@app.route('/status')
def status():
    """
    This function returns the status of LED
    """
    global STATUS
    return STATUS


def cycle_run():
    """ This cycles through the three LEDS like a stoplight
       Args:
       Returns:
       """
    print("LED RUNNING CYCLE")
    global STOP
    global STATUS
    STOP = False
    while True:
        if STOP:
            break
        stoplight.red()
        STATUS = 'red'
        sleep(5)
        if STOP:
            break
        stoplight.green()
        STATUS = 'green'
        sleep(5)
        if STOP:
            break
        stoplight.yellow()
        STATUS = 'yellow'
        sleep(2)
        if STOP:
            break


def cycle_stop():
    """ This stops the cycle of the stoplight
       Args:
       Returns:
       """
    print('STOPPING CYCLE')
    global STOP
    STOP = True
    return


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
