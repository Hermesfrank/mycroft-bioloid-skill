# Code to build a voice-directed Robotis Bioloid robot with LED face animations.
# 2022-01-14  FBH  Have RPi 4 talking to robot

from mycroft import MycroftSkill, intent_file_handler

from .actions_motions import *


class MycroftBioloidSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('forward.intent')
    def handle_forward(self, message):
        move_forward()
        self.speak_dialog('forward')


def create_skill():
    return MycroftBioloidSkill()