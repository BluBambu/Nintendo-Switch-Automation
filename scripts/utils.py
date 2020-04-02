#!/usr/bin/env python3

import serial
from enum import Enum

ser = None

class Button(Enum):
    A = "A"
    B = "B"
    X = "X"
    Y = "Y"
    L = "L"
    R = "R"
    ZL = "ZL"
    ZR = "ZR"
    HOME = "HOME"


def initialize_serial(port:str):
    global ser
    ser = serial.Serial('COM3', 9600)


def __send_command(msg:str):
    for msg_char in msg:
        msg_char_input = f'{msg_char}'.upper().encode('utf-8')
        ser.write(msg_char_input)
        msg_char_output = ser.read()
        assert msg_char_input is msg_char_output


def press(btn:Button):
    __send_command('Button %s\r\n' % btn.value)
