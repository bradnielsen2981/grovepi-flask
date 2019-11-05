''' This file will provide an interface to your GrovePi code. The functions should accept the port, so to make them port independent. '''
import grovepi
import time
import logging

log = logging.getLogger('app')

# This function will return the current light reading from the desired ANALOG port A0, A1 etc
def read_light_sensor_analogueport(port):
    light_sensor = port
    grovepi.pinMode(light_sensor,"INPUT")
    sensor_value = None
    try:
        sensor_value = grovepi.analogRead(light_sensor) # Get sensor value
    except IOError:
        log.error("Error in reading the light sensor")
    return sensor_value

#Turn on the led
def turn_on_led_digitalport(port):
    led = port
    grovepi.pinMode(led,"OUTPUT")
    grovepi.digitalWrite(led,255)
    return

#Turn off the led
def turn_off_led_digitalport(port):
    led = port
    grovepi.pinMode(led,"OUTPUT")
    grovepi.digitalWrite(led,0)
    return



#--------------------------------------------------------------------
#Only execute if this is the main file, good for testing code
if __name__ == '__main__':
    pass
    '''
    while True:
        light = read_light_sensor_analogueport(0)
        print(light)
    '''

