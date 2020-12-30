#!/usr/bin/env python
"""
info about project here
"""

import multiprocessing
import time

from gpiozero import Button, LED
from gpiozero.pins.pigpio import PiGPIOFactory

...

__author__ = "Johannes Coolen"
__email__ = "johannes.coolen@student.kdg.be"
__status__ = "development"


IP = PiGPIOFactory(host='192.168.0.196')
BUTTON1 = Button(pin=4, pin_factory=IP, pull_up=True,  bounce_time=0.3)
BUTTON2 = Button(pin=5, pin_factory=IP, pull_up=True,  bounce_time=0.3)
BUTTON3 = Button(pin=6, pin_factory=IP, pull_up=True,  bounce_time=0.3)
LED1 = LED(pin=17, pin_factory=IP)
LED2 = LED(pin=18, pin_factory=IP)
LED3 = LED(pin=19, pin_factory=IP)


def wacht_knop1():
    while 0<1:
        if BUTTON1.is_pressed:
            LED1.on()
            time.sleep(5)
            LED1.off()


def wacht_knop2():
    while True:
        if BUTTON2.is_pressed:
            LED2.on()
            time.sleep(5)
            LED2.off()


def wacht_knop3():
    while True:
        if BUTTON3.is_pressed:
            LED3.on()
            time.sleep(5)
            LED3.off()


if __name__ == '__main__':  # code to execute if called from command-line
    PROCESS_ONE = multiprocessing.Process(target=wacht_knop1)
    PROCESS_TWO = multiprocessing.Process(target=wacht_knop2)
    PROCESS_THREE = multiprocessing.Process(target=wacht_knop3)

    PROCESS_ONE.start()
    PROCESS_TWO.start()
    PROCESS_THREE.start()
