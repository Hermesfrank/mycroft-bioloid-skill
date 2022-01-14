import serial
import time

# open serial port
ser = serial.Serial(port='/dev/ttyUSB0', baudrate=57600, timeout=1)


class Motions(object):
    """Class used to define which command(s) to send to robot
    """

# --> Sub callback function, one per intent

    def move_forward(self,message):

        # action code goes here...

        #    actions_leds.initialize_pi_hat_leds()

        # send command to bot
        ser.write(b'\xFF\x55\x01\xFE\x00\xFF')
        # terminates action at one step
        ser.write(b'\xFF\x55\x00\xFF\x00\xFF')
