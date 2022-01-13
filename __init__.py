from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
from mycroft.util.log import LOG

# import requests


class MycroftBioloidSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('forward.intent')
    def handle_forward(self, message):
        self.speak_dialog('forward')


def create_skill():
    return MycroftBioloidSkill()

