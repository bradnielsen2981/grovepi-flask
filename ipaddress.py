# Python Program to Get IP Address   
import socket
import time
import uuid
from grove_rgb_lcd import *

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def get_macaddress():
    return hex(uuid.getnode())

#Only execute if this is the main file, good for testing code
if __name__ == '__main__':
    setRGB(0,128,64)

    elapsedtime = 0
    starttime = time.time()
    c = 1
    diff = 1
    # Slowly change the colors every 0.01 seconds.
    while elapsedtime < 120:
        elapsedtime = time.time() - starttime
        setText(get_ip() + " " + get_macaddress())
        setRGB(c,255-c,0)
        time.sleep(0.01)
        if c == 255 or c==0:
            diff = -diff
        c+=diff
    setRGB(0,0,0) #not sure how to turn off
    setText("")