# Code to build a voice-directed Robotis Bioloid robot with LED face animations.
# 2022-01-14  FBH  Have RPi 4 talking to robot

from mycroft import MycroftSkill, intent_file_handler

from .actions_motions import *
from .actions_leds import *
import time

# Using an Adafruit DotStar 8x8 LED Matrix connected to digital pins 12 and 13 to make faces - see actions_leds module
# Initialize face LED-matrix to all off
initialize_matrix()
# Initialize basic neutral face
initialize_face()
# Initialize Respeaker LEDs
initialize_pi_hat_leds()


class MycroftBioloidSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    # chat
    @intent_file_handler('smile.intent')
    def handle_smile(self, message):
        self.speak_dialog('smile')
        smile()
        time.sleep(5)
        straight_face()

    @intent_file_handler('frown.intent')
    def handle_frown(self, message):
        self.speak_dialog('frown')
        frown()
        time.sleep(5)
        straight_face()

    @intent_file_handler('wink.intent')
    def handle_wink(self, message):
        self.speak_dialog('wink')
        wink()

    @intent_file_handler('belong_to.intent')
    def handle_when_belong_to(self, message):
        self.speak_dialog('belong_to')
        initialize_pi_hat_leds()


    # actions
    @intent_file_handler('forward.intent')
    def handle_forward(self, message):
        self.speak_dialog('forward')
        move_forward()

    @intent_file_handler('backward.intent')
    def handle_backward(self, message):
        self.speak_dialog('backward')
        move_back()


def create_skill():
    return MycroftBioloidSkill()