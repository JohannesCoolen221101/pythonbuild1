#!/usr/bin/env python
"""
info about project here
"""

import multiprocessing
import time
from gpiozero import Button, LED
from gpiozero.pins.pigpio import PiGPIOFactory
from guizero import App, Window, PushButton

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


def toggle_Led1():
    while True:
        if BUTTON1.is_pressed:
            LED1.toggle()
            time.sleep(1)
        if button1.text == "off":
            button1.text = "on"
        elif button1.text == "on":
            button1.text = "off"



def toggle_Led2():
    while True:
        if BUTTON2.is_pressed:
            LED2.toggle()
            time.sleep(1)
        if button2.text == "off":
            button2.text = "on"
        elif button2.text == "on":
            button2.text = "off"


def toggle_Led3():
    while True:
        if BUTTON3.is_pressed:
            LED3.toggle()
            time.sleep(1)
        if button3.text == "off":
            button3.text = "on"
        elif button3.text == "on":
            button3.text = "off"


def toggle_LED1():
    LED1.toggle()
    time.sleep(1)
    if button1.text == "off":
        button1.text = "on"
    elif button1.text == "on":
        button1.text = "off"


def toggle_LED2():
    LED2.toggle()
    time.sleep(1)
    if button2.text == "off":
        button2.text = "on"
    elif button2.text == "on":
        button2.text = "off"


def toggle_LED3():
    LED3.toggle()
    time.sleep(1)
    if button3.text == "off":
        button3.text = "on"
    elif button3.text == "on":
        button3.text = "off"


app = App()                                             #app initialiseren
button1 = PushButton(app, text="off", align="left")     #knoppen aanmaken
button2 = PushButton(app, text="off", align="left")
button3 = PushButton(app, text="off", align="left")
button1.when_clicked = toggle_LED1                      #knoppen functionaliteit geven
button2.when_clicked = toggle_LED2
button3.when_clicked = toggle_LED3
app.display()                                           #app laten zien

if __name__ == '__main__':  # code to execute if called from command-line
    PROCESS_ONE = multiprocessing.Process(target=toggle_Led1)
    PROCESS_TWO = multiprocessing.Process(target=toggle_Led2)
    PROCESS_THREE = multiprocessing.Process(target=toggle_Led3)

    PROCESS_ONE.start()
    PROCESS_TWO.start()
    PROCESS_THREE.start()

