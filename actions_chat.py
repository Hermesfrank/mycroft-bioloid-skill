from .actions_leds import *
import os

def make_wink():
    initialize_pi_hat_leds()
    wink()

def make_smile():
    initialize_pi_hat_leds()
    smile()
    time.sleep(4)
    straight_face()

def make_frown():
    initialize_pi_hat_leds()
    frown()
    time.sleep(4)
    straight_face()

def belong_to():
    initialize_pi_hat_leds()

def terminate():
    initialize_pi_hat_leds()
    os.system("shutdown /s /t 0")