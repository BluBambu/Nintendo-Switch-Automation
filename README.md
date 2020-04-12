# Nintendo Switch Automation

## Summary

Automate menial tasks on the Nintendo Switch with Arduino:

[![Thumbnail](https://i.imgur.com/cJLZUdhl.jpg)](https://twitter.com/ebith/status/954858876028907521)

This involves:
  1. Using an Arduino to emulate a Nintendo Switch controller.
  2. Controlling the fake controller via a python script on the PC.

## Necessary Items
- ATMega16U2 or ATMega32U4 board such as the Arduino UNO Rev3.
- USB to serial adapter.
- USB micro-b to USB c cable to connect Arduino to the Ninteno Switch.
- USB A female to USB A male to connect USB to serial adapter to PC.
- 3 male to male jumper cables.

## Usage

1. Run `make` and flash Joystick.hex onto the Arduino.
2. Connect the USB to serial GND to Arduino GND pin.
3. Connect the USB to serial RXD to Arduino TX pin.
4. Connect the USB to serial TXD to Arduino RX pin.
5. Connect the USB to serial to the PC.
6. Connect the Arduino to the Nintendo Switch.
7. Run the python script to have the Arduino send controller input to the Ninteno Switch. See `scripts` for examples.
