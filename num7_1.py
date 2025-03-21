import RPi.GPIO as GPIO
import time



MAXV = 201
MINV = 168

led =   [ 2,  3,  4, 17, 27, 22, 10,  9]
dac =   [ 8, 11,  7,  1,  0,  5, 12,  6]
comp =   14
troyka = 13


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)








def dec2bin(x):
    return [int(elem) for elem in bin(x)[2:].zfill(8)]


def bin2dec(x):
    return int(''.join([str(i) for i in x]), base = 2)


def adc():
    signal = [0] * 8
    for i in range(8):
        signal[i] = 1
        GPIO.output(dac, signal)
        time.sleep(0.007)
        if GPIO.input(comp):
            signal[i] = 0
    return bin2dec(signal)



try:
    start_time = time.time()
    results = []

    while True:
        
        value = adc()

        # print("value = ", value, "voltage = ", 3.3 * value / 255)
        # GPIO.output(led, dec2bin(value))

        results.append(value)

        if value >  MAXV and GPIO.input(troyka) == GPIO.HIGH:
            GPIO.output(troyka, GPIO.LOW)

        elif value < MINV and GPIO.input(troyka) == GPIO.LOW:
            GPIO.output(troyka, GPIO.HIGH)
            break        

finally:
    end_time = time.time()
    with open("tuning.txt", 'w') as f:
        f.write(f'{(end_time - start_time) / len(results)}\n{3.3 / 256}') 
    
    with open("results.txt", 'w') as f:
        f.write('\n'.join([str(elem) for elem in results]))




    GPIO.output(dac, 0)
    GPIO.output(led, 0)
    GPIO.output (troyka, 0)
    GPIO.cleanup()