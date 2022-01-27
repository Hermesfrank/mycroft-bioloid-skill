import actions_leds
import time


def when_born():
    actions_leds.initialize_pi_hat_leds()


def creator():
    actions_leds.initialize_pi_hat_leds()


def belong_to():
    actions_leds.initialize_pi_hat_leds()


def wink():
    actions_leds.initialize_pi_hat_leds()

    # Wink
    time.sleep(1)
    actions_leds.wink()


def smile():
    actions_leds.initialize_pi_hat_leds()

    # smile
    time.sleep(1)
    actions_leds.smile()
    time.sleep(5)
    actions_leds.straight_face()


def frown():
    actions_leds.initialize_pi_hat_leds()

    # frown
    time.sleep(1)
    actions_leds.frown()
    time.sleep(1)
    actions_leds.straight_face()