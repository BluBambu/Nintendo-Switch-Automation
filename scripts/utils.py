#!/usr/bin/env python3

import serial
from enum import Enum
from time import sleep
import struct

ser = None

class Special(Enum):
    RELEASE = "RELEASE"

class Button(Enum):
    A = "Button A"
    B = "Button B"
    X = "Button X"
    Y = "Button Y"
    L = "Button L"
    R = "Button R"
    ZL = "Button ZL"
    ZR = "Button ZR"
    HOME = "Button HOME"
    SELECT = "Button SELECT"
    START = "Button START"
    LCLICK = "Button LCLICK"
    RCLICK = "Button RCLICK"
    CAPTURE = "Button CAPTURE"
    RELEASE = "Button RELEASE"

class Hat(Enum):
    TOP = "HAT TOP"
    TOP_RIGHT = "HAT TOP_RIGHT"
    RIGHT = "HAT RIGHT"
    BOTTOM_RIGHT = "HAT BOTTOM_RIGHT"
    BOTTOM = "HAT BOTTOM"
    BOTTOM_LEFT = "HAT BOTTOM_LEFT"
    LEFT = "HAT LEFT"
    TOP_LEFT = "HAT TOP_LEFT"
    CENTER = "HAT CENTER"

def initialize_serial(port:str):
    global ser
    ser = serial.Serial('COM3', 9600)

def __send_command(data:int):
    data_binary = struct.pack('>B', data)
    ser.write(data_binary)
    msg_char_output = ser.read()
    assert data_binary == msg_char_output

def press(btn):
    values = Special._member_names_
    values.extend(Button._member_names_)
    values.extend(Hat._member_names_)

    data = values.index(btn.name)
    __send_command(data)
    sleep(0.04)
    __send_command(values.index(Special.RELEASE.name))

def press_rep(btn, repeat_num:int):
    for i in range(repeat_num):
        press(btn)
        sleep(0.04)

def increment_date():
    press(Button.HOME)
    sleep(0.5)
    press(Hat.BOTTOM)
    press_rep(Hat.RIGHT, 4)
    press(Button.A)
    sleep(1)
    press_rep(Hat.BOTTOM, 14)
    press(Button.A)
    sleep(0.25)
    press_rep(Hat.BOTTOM, 4)
    press(Button.A)
    sleep(0.25)
    press_rep(Hat.BOTTOM, 2)
    press(Button.A)
    sleep(0.25)
    press(Hat.RIGHT)
    press(Hat.TOP)
    press_rep(Hat.RIGHT, 5)
    press(Button.A)
    press(Button.HOME)
    sleep(1)
    press(Button.A)
    sleep(1)