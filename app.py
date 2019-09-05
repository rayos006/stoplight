from flask import Flask, render_template, request
import stoplight
from time import sleep
import threading

global STOP

app = Flask(__name__)
application = app


@app.route('/')
def home():
    status = "off"
    # TODO Set led to off
    return render_template('index.html', status=status)


@app.route('/off')
def off():
    if 't' in globals():
        cycle_stop()
        t.join()
    status = 'off'
    stoplight.off()
    return render_template('index.html', status=status)


@app.route('/red')
def red():
    if 't' in globals():
        cycle_stop()
        t.join()
    status = 'red'
    stoplight.red()
    return render_template('index.html', status=status)


@app.route('/yellow')
def yellow():
    if 't' in globals():
        cycle_stop()
        t.join()
    status = 'yellow'
    stoplight.yellow()
    return render_template('index.html', status=status)


@app.route('/green')
def green():
    if 't' in globals():
        cycle_stop()
        t.join()
    status = 'green'
    stoplight.green()
    return render_template('index.html', status=status)


@app.route('/run')
def run():
    global t
    t = threading.Thread(target=cycle_run)
    t.start()
    return render_template('index.html')


def cycle_run():
    """ Changes led to off
       Args:
       Returns:
       """
    print("LED RUNNING CYCLE")
    global STOP
    STOP = False
    while True:
        if STOP:
            break
        stoplight.red()
        status = 'red'
        test('red')
        sleep(5)
        if STOP:
            break
        stoplight.green()
        sleep(5)
        if STOP:
            break
        stoplight.yellow()
        sleep(2)
        if STOP:
            break


def cycle_stop():
    """ Changes led to off
       Args:
       Returns:
       """
    print('STOPPING CYCLE')
    global STOP
    STOP = True
    return


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
