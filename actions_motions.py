import serial
import time

# open serial port
ser = serial.Serial(port='/dev/ttyUSB0', baudrate=57600, timeout=1)


def move_forward():

    # action code goes here...

    #    actions_leds.initialize_pi_hat_leds()

    # send command to bot
    ser.write(b'\xFF\x55\x01\xFE\x00\xFF')
    # terminates action at one step
    ser.write(b'\xFF\x55\x00\xFF\x00\xFF')

def move_backward():

    # action code goes here...

