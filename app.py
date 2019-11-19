from flask import Flask, render_template, jsonify, request
import logging #allow loggings
import grove #imports the grove functionality that you define
import ipaddress #imports the display on I2C-2
from datetime import datetime

#uses JSONIFY to encode data structures in Strings. AJAX can then change it back..

#Global Variables
app = Flask(__name__)
log = app.logger #sets up a log -- to log call log.info('message')
#log.error("Testing") --use this to log an error

#request handlers ---------------------------------------------
@app.route('/')
def home():
    return render_template("index.html")

#start a light
@app.route('/start', methods=['GET','POST'])
def start():
    grove.turn_on_led_digitalport(5) #turn on led on d5
    return jsonify({ "message":"starting" }) #jsonify take any type and makes a JSON string

#stop a light
@app.route('/stop', methods=['GET','POST'])
def stop():
    grove.turn_off_led_digitalport(5) #turn off led on d5
    return jsonify({ "message":"stopping" }) 

#start RGB display
@app.route('/displayipaddress', methods=['GET','POST'])
def displayipaddress():
    ipaddress.run_ipaddress_RGB_display() #set ipaddress RGB
    return jsonify({ "message":"running ipaddress display" })

#start RGB display
@app.route('/getlightlevel', methods=['GET','POST'])
def getlightlevel():
    light = grove.read_light_sensor_analogueport(1) #get light sensor from a1
    lightreading = "Light level: " + str(light)
    log.error(lightreading)
    return jsonify({ "message":lightreading })

#start RGB display
@app.route('/getlight', methods=['GET','POST'])
def getlight():
    light = grove.read_light_sensor_analogueport(1) #get light sensor from a1
    return jsonify({ "Light":light })

#display chart using chart.js
@app.route('/realtimechart', methods=['GET','POST'])
def realtimechart():
    if request.method == "POST":
        light = grove.read_light_sensor_analogueport(1)
        time = datetime.now()
        return jsonify({"Time":time.second,"Light":light,"Temperature":0})
    else:
        return render_template('realtimechart.html')

#---------------------------------------------------------------
#Shutdown the web server
@app.route('/shutdown', methods=['GET','POST'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    func()
    return jsonify({ "message":"shutting down" }) 

#Threaded mode is important if using shared resources e.g. sensor, each user request launches a thread.. 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
