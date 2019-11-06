''' This file will provide an interface to your GrovePi code. Write functions to accept the port argument, so to make them port independent. Try to name your functions to indicate the type of port e.g. read_light_analogueport '''
import grovepi
import time
import logging

log = logging.getLogger('app')

# This function will return the current light reading from the desired ANALOG port A0, A1 etc
def read_light_analogueport(port):
    light_sensor = port
    grovepi.pinMode(light_sensor,"INPUT")
    sensor_value = None
    try:
        sensor_value = grovepi.analogRead(light_sensor) # Get sensor value
    except IOError:
        log.error("Error in reading the light sensor")
    return sensor_value

def read_ultrasonic_digitalport(port):
    sensor_value = None
    # ensure port is set to input
    # use a try and except block same as above to log error
    # use grovepi.ultrasonicRead()
    return sensor_value

#Turn on the led
def turn_on_led_digitalport(port):
    #insert output pincode here...255 is bright
    #digital write 255 is bright
    return

#Turn off the led
def turn_off_led_digitalport(port):
    # ensure port is set to output
    # digitalwrite 0 is dark
    return

def turn_off_buzzer_digitalport(port):
    # ensure port is set to output
    # digitalwrite 0
    return

def turn_off_buzzer_digitalport(port):
    # ensure port is set to output
    # digitalwrite 1
    return

#--------------------------------------------------------------------
# Main program goes here. This code is only called if the file is the execution point
if __name__ == '__main__':
    pass #remove this
    ''' #uncomment by deleting quotations marks
    while True: #forever loop
        # read ultrasonic distance
        # if ultrasonic distance < 20
            # turn on led 
            # play buzzer
            # sleep for 3 seconds
            # turn off led
            # turn off buzzer
    '''

