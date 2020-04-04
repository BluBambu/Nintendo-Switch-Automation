#!/usr/bin/env python3

from utils import *

def main():
    initialize_serial('COM3')

    // Click through title menu
    press(Button.A)
    sleep(5)
    press(Button.A)

    # increment_date()

if __name__ == "__main__":
    main()