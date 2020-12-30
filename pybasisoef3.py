#!/usr/bin/env python
"""
info about project here
"""
import time

from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory

...

__author__ = "Johannes Coolen"
__email__ = "johannes.coolen@student.kdg.be"
__status__ = "development"


IP = PiGPIOFactory(host='192.168.0.196')

BUTTON_UP = Button(pin=4, pin_factory=IP, pull_up=True,  bounce_time=0.3)
BUTTON_DOWN = Button(pin=5, pin_factory=IP, pull_up=True,  bounce_time=0.3)
BUTTON_RESET = Button(pin=6, pin_factory=IP, pull_up=True,  bounce_time=0.3)


def main():
    x = 0
    while True:

        if BUTTON_UP. is_pressed:
            x += 1
            print(x)
            time.sleep(0.5)

        if BUTTON_DOWN.is_pressed:
            x -= 1
            print(x)
            time.sleep(0.5)

        if BUTTON_RESET.is_pressed:
            x = 0
            print(x)
            time.sleep(0.5)


if __name__ == '__main__':  # code to execute if called from command-line
    main()
