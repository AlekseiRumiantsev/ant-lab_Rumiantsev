import RPi.GPIO as GPIO

def dec2bin(x):
    return [int(elem) for elem in bin(x)[2:].zfill(8)]



led = [2,3,4,17,27,22,10,9]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
a = [0, 1] * 4


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)

try:
    while True:

        user = input("Введите число от 0 до 255:   ")

        if user == 'q':
            print("Quit!")
            exit()
        if not user.isdigit() or not isinstance(int(user), int):
            print("not int!")
            exit()
        if int(user) < 0 or int(user) > 255:
            print("number must belong from 0 to 255")
            exit()


        a = dec2bin(int(user))
        print(3.3 *(int(user)/255))
        GPIO.output(dac, a)

finally:
    GPIO.output(dac, 0)
    GPIO.output(led, 0)

    GPIO.cleanup()
