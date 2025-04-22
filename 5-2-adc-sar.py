import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec2bin(num):
    return [int(elem) for elem in bin(num)[2:].zfill(8)]

def adc():
    i = 255
    val = 0
    while i > 1:
        GPIO.output(dac, dec2bin(val+i)[0:8])
        time.sleep(0.01)
        if GPIO.input(comp) == GPIO.LOW:
            val += i
        i //= 2

    val = min(val, 255)
    return val

try:
    while 1:
       i = adc()
       voltage = i * 3.3 / 256.0
       
       if i: print("{:.2f} V".format(voltage))

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()