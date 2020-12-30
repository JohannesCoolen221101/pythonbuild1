#!/usr/bin/env python
"""
info about project here
"""
import multiprocessing
from time import sleep


...

__author__ = "Johannes Coolen"
__email__ = "johannes.coolen@student.kdg.be"
__status__ = "development"





def eensec():
    x=0
    while True:
        sleep(1)
        print(x)
        x +=1



def tweesec():
    y=0
    while True:
        sleep(2)
        print(y)
        y+=1


if __name__ == '__main__':  # code to execute if called from command-line
    PROCESS_ONE = multiprocessing.Process(target=eensec)
    PROCESS_TWO = multiprocessing.Process(target=tweesec)
    PROCESS_ONE.start()
    PROCESS_TWO.start()
