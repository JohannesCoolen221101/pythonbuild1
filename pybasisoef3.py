#!/usr/bin/env python
"""
info about project here
"""

from gpiozero import Button

...

__author__ = "Johannes Coolen"
__email__ = "johannes.coolen@student.kdg.be"
__status__ = "development"


BUTTON_UP = Button(pin=4, pin_factory=None)
BUTTON_DOWN = Button(pin=5, pin_factory=None)
BUTTON_RESET = =Button(pin=6, pin_factory=None)


def main():
    x = 0


    while True:

        if BUTTON_UP. is_pressed():
            x += 1
            print(x)
        if BUTTON_DOWN.is_pressed():
            x -= 1
            print(x)
        if BUTTON_RESET.is_presser():
            x=0
            print(x)


if __name__ == '__main__':  # code to execute if called from command-line
    main()
