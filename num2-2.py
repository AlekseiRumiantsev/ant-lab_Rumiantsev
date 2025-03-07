import RPi.GPIO as GPIO
import time
# import random

def my_bin(x):
    x = list('{:08b}'.format(x))
    for i in range(len(x)):
        x[i] = int(x[i])
    return(x)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0, 1] * 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
# random.shuffle(number)
# GPIO.output(dac, number)
# time.sleep(15)

numbers = sorted([2, 255, 127, 64, 32, 5, 0, 256])
for i in numbers:
    current_num = my_bin(i)
    GPIO.output(dac, current_num)
    print(i, current_num)
    time.sleep(15)
    GPIO.output(dac, 0)
    time.sleep(0.5)


GPIO.output(dac, 0)
GPIO.cleanup()




