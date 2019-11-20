from flask import Flask, render_template, jsonify, request
import logging #allow loggings
import grove #imports the grove functionality that you define

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
    #call the grove pi led turn on code
    return jsonify({ "message":"starting" }) #jsonify take any type and makes a JSON string

#stop a light
@app.route('/stop', methods=['GET','POST'])
def stop():
    #call the grove pi led turn off code
    return jsonify({ "message":"stopping" }) 

#---------------------------------------------------------------
#Shutdown the web server
@app.route('/shutdown', methods=['GET','POST'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    func()
    return jsonify({ "message":"shutting down" }) 

#Threaded most is useful if multiple users are logging but causes issues
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=False)
