"""
This file contains all the code used to interface with the Raspberry Pi Pico W
over bluetooth
"""

import socket

s = socket.socket(family=socket.AF_BLUETOOTH)
