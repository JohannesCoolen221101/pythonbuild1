#!/usr/bin/env python
"""
info about project here
"""

from gpiozero import LED
import time
from gpiozero.pins.pigpio import PiGPIOFactory


__author__ = "Johannes Coolen"
__email__ = "johannes.coolen@student.kdg.be"
__status__ = "development"


IP = PiGPIOFactory(host='192.168.0.196')
LED = LED(pin=17, pin_factory=IP)


def main():
    LED.on()
    time.sleep(5)
    LED.off()
    for x in range(5):
        time.sleep(2)
        LED.on()
        time.sleep(2)
        LED.off()
    while True:
        time.sleep(1)
        LED.on()
        time.sleep(1)
        LED.off()


if __name__ == '__main__':  # code to execute if called from command-line
    main()
