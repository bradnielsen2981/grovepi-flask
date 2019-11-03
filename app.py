from flask import *
import os
#import picamera
#import cv2 #this might need certain libraries to be installed

#Global Variables
app = Flask(__name__)

#request handlers ---------------------------
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/start')
def start():
    return("Start")

@app.route('/stop')
def stop():
    return("Stop")

@app.route('/shutdown')
def shoutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    func()
    return("Shutdown Flask Server")

#Needs to be in its own file
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

#Threaded mode is important if using shared resources e.g. sensor, each user request launches a thread.. 
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
