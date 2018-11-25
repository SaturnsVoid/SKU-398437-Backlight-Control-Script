"""
Simple Backlight control script for the 2.2inch TFT Display SKU:398437
Version: 0.1
https://github.com/SaturnsVoid

"""

from gpiozero  import Button
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.OUT)

button = Button(4)

isON = True

while True:
        if (isON) and (button.is_pressed):
                isON = False
                GPIO.output(27, GPIO.LOW)
                print "Screen OFF"

        elif (not isON) and (button.is_pressed):
                isON = True
                GPIO.output(27, GPIO.HIGH)
                print "Screen ON"
        sleep(1)
