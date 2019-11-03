from flask import *
import os

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
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    func()
    return("Shutdown Flask Server")

#Threaded mode is important if using shared resources e.g. sensor, each user request launches a thread.. 
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
