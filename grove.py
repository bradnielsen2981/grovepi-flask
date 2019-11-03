''' This file will provide an interface to your GrovePi code. The functions should accept the port, so to make them port independent. '''

import grovepi
import time

# Connect the LED to digital port D5
led = 5
grovepi.pinMode(led,"OUTPUT")

# This function will return the current light reading from the desired ANALOG port A0, A1 etc
def read_light_sensor_from_port(port):
    light_sensor = port
    grovepi.pinMode(light_sensor,"INPUT")
    sensor_value = None
    try:
        # Get sensor value
        sensor_value = grovepi.analogRead(light_sensor)
    except IOError:
        print("Error in reading the light sensor")
    except:
        print("Error ??")

    return sensor_value


while True:
    light = read_light_sensor_from_port(0)
    print(light)
    grovepi.digitalWrite(led,light)
    time.sleep(0.5)

