import RPi.GPIO as GPIO
#import time


def dec2bin(x):
    return [int(elem) for elem in bin(x)[2:].zfill(8)]



led = [2,3,4,17,27,22,10,9]

aux = 21
duty_cycle = 0

GPIO.setmode(GPIO.BCM)

GPIO.setup(aux, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)

GPIO.output(led, 0)

try:
    while True:
        p = GPIO.PWM(aux, 1)
        p.start(duty_cycle)
        duty_cycle = int(input("Введите коэф. заполнения: "))
        print(0.01 * duty_cycle * 3.3)
        p.stop()


finally:
    GPIO.output(aux, 0)

    GPIO.cleanup()
