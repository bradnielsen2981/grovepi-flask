from flask import *
import brickpirobot # import the BrickPi3 helpers
#from raspberry import RaspberryThread
import os
import picamera
#import cv2
import socket
import io

#Global Variables
#vc = cv2.VideoCapture(0)
robot = brickpirobot.Robot()

app = Flask(__name__)

#request handlers ---------------------------

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/start')
def start():
    robot.move_power_untildistanceto(25,10)
    #robot.move_time_power(10,25)
    return("Start")

@app.route('/stop')
def stop():
    robot.stop_all()
    return("Stop")

@app.route('/resetall')
def resetall():
    robot.reset_all()
    return("Reset All")


#---------------CAMERA FUNCTIONS-------------------NEED TO INSTALL OPENCV
'''def gen():
    """Video streaming generator function."""
    while True:
        rval, frame = vc.read()
        cv2.imwrite('t.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('t.jpg', 'rb').read() + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
'''
#--------------------------------------------#

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)