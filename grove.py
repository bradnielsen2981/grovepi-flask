''' This file will provide an interface to your GrovePi code. The functions should accept the port, so to make them port independent. '''
import grovepi
import time
import logging

log = logging.getLogger('app.grove')

# This function will return the current light reading from the desired ANALOG port A0, A1 etc
def read_light_sensor_from_port(port):
    light_sensor = port
    grovepi.pinMode(light_sensor,"INPUT")
    sensor_value = None
    try:
        sensor_value = grovepi.analogRead(light_sensor) # Get sensor value
    except IOError:
        log.info("Error in reading the light sensor")
    return sensor_value

#Only execute if this is the main file, good for testing code
if __name__ == '__main__':
    while True:
        light = read_light_sensor_from_port(0)
        print(light)
        # Connect the LED to digital port D5
        led = 5
        grovepi.pinMode(led,"OUTPUT")
        grovepi.digitalWrite(led,light)
        time.sleep(0.5)

