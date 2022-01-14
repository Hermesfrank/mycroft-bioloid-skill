# from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler
# from mycroft.util.log import LOG

# import requests
# import serial
import actions_motion

# open serial port
3 ser = serial.Serial(port='/dev/ttyUSB0', baudrate=57600, timeout=1)


class MycroftBioloidSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('forward.intent')
    def handle_forward(self, message):

        # send command to bot
#        ser.write(b'\xFF\x55\x01\xFE\x00\xFF')
        # terminates action at one step
#        ser.write(b'\xFF\x55\x00\xFF\x00\xFF')

        actions_motion.move_forward

        self.speak_dialog('forward')


def create_skill():
    return MycroftBioloidSkill()