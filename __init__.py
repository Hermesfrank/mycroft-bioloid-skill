# Code to build a voice-directed Robotis Bioloid robot with LED face animations.
# 2022-01-14  FBH  Have RPi 4 talking to robot

from mycroft import MycroftSkill, intent_file_handler

#import actions_leds
from .actions_motions import *
#from .actions_leds import *
from .actions_chat import *
#import time

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

    # CHAT ##################################
    @intent_file_handler('make_smile.intent')
    def handle_make_smile(self, message):
        self.speak_dialog('make_smile')
        make_smile()

    @intent_file_handler('make_frown.intent')
    def handle_make_frown(self, message):
        self.speak_dialog('make_frown')
        make_frown()

    @intent_file_handler('make_wink.intent')
    def handle_make_wink(self, message):
        self.speak_dialog('make_wink')
        make_wink()

    @intent_file_handler('belong_to.intent')
    def handle_when_belong_to(self, message):
        self.speak_dialog('belong_to')
        belong_to()


    # MOTIONS ################################
    @intent_file_handler('forward.intent')
    def handle_forward(self, message):
        self.speak_dialog('forward')
        move_forward()

    @intent_file_handler('backward.intent')
    def handle_backward(self, message):
        self.speak_dialog('backward')
        move_back()

    @intent_file_handler('turn_right.intent')
    def handle_turn_right(self, message):
        self.speak_dialog('turn_right')
        turn_right()

    @intent_file_handler('turn_left.intent')
    def handle_turn_left(self, message):
        self.speak_dialog('turn_left')
        turn_left()

    @intent_file_handler('handstand.intent')
    def handle_handstand(self, message):
        self.speak_dialog('handstand')
        do_handstand()

    @intent_file_handler('pushup.intent')
    def handle_pushup(self, message):
        self.speak_dialog('pushup')
        do_pushup()

    @intent_file_handler('pound.intent')
    def handle_pound(self, message):
        self.speak_dialog('pound')
        pound_chest()


def create_skill():
    return MycroftBioloidSkill()