import serial
import time
from .actions_leds import *

# open serial port
ser = serial.Serial(port='/dev/ttyUSB0', baudrate=57600, timeout=1)


def move_forward():
    # action code goes here...
    initialize_pi_hat_leds()

    # send command to bot
    ser.write(b'\xFF\x55\x01\xFE\x00\xFF')
    # terminates action at one step
    ser.write(b'\xFF\x55\x00\xFF\x00\xFF')

def move_back():
    # action code goes here...
    initialize_pi_hat_leds()

    # send command to bot
    ser.write(b'\xFF\x55\x02\xFD\x00\xFF')
    # terminates action at one step
    ser.write(b'\xFF\x55\x00\xFF\x00\xFF')

def turn_right():
    # action code goes here...
    initialize_pi_hat_leds()

    # send command to bot
    ser.write(b'\xFF\x55\x08\xF7\x00\xFF')
    # terminates action at one step
    ser.write(b'\xFF\x55\x00\xFF\x00\xFF')

def turn_left():
    # action code goes here...
    initialize_pi_hat_leds()

    # send command to bot
    ser.write(b'\xFF\x55\x04\xFB\x00\xFF')
    # terminates action at one step
    ser.write(b'\xFF\x55\x00\xFF\x00\xFF')


