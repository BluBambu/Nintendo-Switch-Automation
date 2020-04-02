#!/usr/bin/env python3

from utils import *

def main():
    initialize_serial('COM3')

    press(Button.A)
    press(Button.B)


if __name__ == "__main__":
    main()