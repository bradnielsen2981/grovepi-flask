from flask import *
import os
#import picamera
#import cv2 #this might need certain libraries to be installed

#Global Variables
app = Flask(__name__)

#for encrypting the password in the database
def hash_password(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

#for decrypting the password in the database - returns true if correct
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

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

@app.route('/resetall')
def resetall():
    return("Reset All")

#Threaded mode is important if using shared resources e.g. sensors, each user request launches a thread.. 
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)