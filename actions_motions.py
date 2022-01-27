import serial
from .actions_leds import *

# open serial port; RPi talks to robot controller this way
ser = serial.Serial(port='/dev/ttyUSB0', baudrate=57600, timeout=1)


def move_forward():
    # flicker the Respeaker 2-min Hat's three LEDs
    initialize_pi_hat_leds()

    # send command to bot
    ser.write(b'\xFF\x55\x01\xFE\x00\xFF')
    # terminates action at one step
    ser.write(b'\xFF\x55\x00\xFF\x00\xFF')

def move_back():
    initialize_pi_hat_leds()

    ser.write(b'\xFF\x55\x02\xFD\x00\xFF')
    # terminates action at one step
    ser.write(b'\xFF\x55\x00\xFF\x00\xFF')

def turn_right():
    initialize_pi_hat_leds()

    ser.write(b'\xFF\x55\x08\xF7\x00\xFF')
    # terminates action at one step
    ser.write(b'\xFF\x55\x00\xFF\x00\xFF')

def turn_left():
    initialize_pi_hat_leds()

    ser.write(b'\xFF\x55\x04\xFB\x00\xFF')
    # terminates action at one step
    ser.write(b'\xFF\x55\x00\xFF\x00\xFF')

def do_handstand():
    initialize_pi_hat_leds()

    ser.write(b'\xFF\x55\x18\xE7\x00\xFF')

def do_pushup():
    initialize_pi_hat_leds()

    ser.write(b'\xFF\x55\x14\xEB\x00\xFF')

def pound_chest():
    initialize_pi_hat_leds()

    # have him smile
    smile()

    # send command to bot
    ser.write(b'\xFF\x55\x21\xDE\x00\xFF')

    # return to normal face
    time.sleep(3)
    straight_face()