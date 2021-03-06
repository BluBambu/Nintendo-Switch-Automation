#!/usr/bin/env python3

from utils import *

def main():
    initialize_serial('COM3')

    boxes_to_clear = 33

    for i in range(boxes_to_clear):
        for x in range(6):
            for y in range(5):
                sleep(0.1)
                
                if y is not 4:
                    press(Hat.BOTTOM)
                    sleep(0.2)
            if x is not 5:
                press(Hat.RIGHT)
                press_rep(Hat.TOP, 4)
        press_rep(Hat.TOP, 4)
        press_rep(Hat.LEFT, 5)
        press(Button.R)
        sleep(0.5)


if __name__ == "__main__":
    main()