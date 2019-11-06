# Python Program to Get IP Address   
import socket
import time
from grove_rgb_lcd import *
import re, uuid 

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

def get_mac():
    return(':'.join(re.findall('..', '%012x' % uuid.getnode())))

#Only execute if this is the main file, good for testing code
if __name__ == '__main__':
    setRGB(0,128,64)
    setText(get_ip() + "  " + get_mac())
    elapsedtime = 0
    starttime = time.time()
    c = 1
    diff = 1
    # Slowly change the colors every 0.01 seconds.
    while elapsedtime < 120:
        elapsedtime = time.time() - starttime
        setRGB(c,255-c,0)
        if c == 255 or c==0:
            diff = -diff
        c+=diff  
        time.sleep(0.1)
    setRGB(0,0,0) #not sure how to turn off
    setText("")