# Code to build a voice-directed Robotis Bioloid robot with LED face animations.
# 2022-01-14  FBH  Have RPi 4 talking to robot

from mycroft import MycroftSkill, intent_file_handler

from .actions_motions import *
from .actions_leds import *

# Using an Adafruit DotStar 8x8 LED Matrix connected to digital pins 12 and 13 to make faces - see actions_leds module
# Initialize face LED-matrix to all off
initialize_matrix()
# Initialize basic neutral face
initialize_face()


class MycroftBioloidSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    # actions
    @intent_file_handler('forward.intent')
    def handle_forward(self, message):
        move_forward()
        self.speak_dialog('forward')

    @intent_file_handler('backward.intent')
    def handle_forward(self, message):
        move_back()
        self.speak_dialog('backward')


def create_skill():
    return MycroftBioloidSkill()