#!/usr/bin/env python
"""
info about project here
"""

from gpiozero import LED
import time

__author__ = "Johannes Coolen"
__email__ = "johannes.coolen@student.kdg.be"
__status__ = "development"


def main():
    led = LED(17)
    led.on()
    time.sleep(5)
    led.off()
    for x in range(5):
        time.sleep(2)
        led.on()
        time.sleep(2)
        led.off()
    while(True):
        time.sleep(1)
        led.on()
        time.sleep(1)
        led.off()

if __name__ == '__main__':  # code to execute if called from command-line
    main()
