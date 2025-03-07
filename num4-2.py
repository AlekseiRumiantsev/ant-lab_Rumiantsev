import RPi.GPIO as GPIO
import time


def dec2bin(x):
    return [int(elem) for elem in bin(x)[2:].zfill(8)]



led = [2,3,4,17,27,22,10,9]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
a = [0, 1] * 4


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)

try:
    T = int(input("Введите период!(секунды) "))
    T = T/256
    while True:
        for cur in range(255):
            GPIO.output(dac, dec2bin(cur))
            print(cur)
            time.sleep(T)
        for cur in range(255, -1, -1):
            GPIO.output(dac, dec2bin(cur))
            print(cur)
            time.sleep(T)


finally:
    GPIO.output(dac, 0)
    GPIO.output(led, 0)

    GPIO.cleanup()
