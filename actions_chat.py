from .actions_leds import *

def make_wink():
    initialize_pi_hat_leds()
    wink()

def make_smile():
    initialize_pi_hat_leds()
    smile()
    time.sleep(5)
    straight_face()

def make_frown():
    initialize_pi_hat_leds()
    frown()
    time.sleep(5)
    straight_face()

def belong_to():
    initialize_pi_hat_leds()

