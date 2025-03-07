import RPi.GPIO as GPIO
import time


leds = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)

for current_led in leds * 3:
    GPIO.output(current_led, 1)
    time.sleep(0.2)
    GPIO.output(current_led, 0)


# time.sleep(3)
GPIO.output(leds, 0)
GPIO.cleanup()


