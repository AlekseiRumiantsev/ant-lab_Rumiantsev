import RPi.GPIO as GPIO
import time


def dec2bin(x):
    return [int(elem) for elem in bin(x)[2:].zfill(8)]

def adc():
    for value in range(256):
        signal = [int(elem) for elem in bin(value)[2:].zfill(8)]
        GPIO.output(dac, signal)
        time.sleep(0.007)
        if GPIO.input(comp) == 1:
            voltage = value * 3.3 / 256
            print("signal = ", signal, "voltage = ", voltage)
            break

led = [2,3,4,17,27,22,10,9]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
a = [0, 1] * 4


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)


try:
    while True:
        adc()

finally:
    GPIO.output(dac, 0)
    GPIO.output(led, 0)
    GPIO.output (troyka, 0)
    GPIO.cleanup()
