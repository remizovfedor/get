import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
leds = [9,10,22,27,17,4,3,2]

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)

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
        adc_val = adc()
        led_vals = [1 if  (adc_val - i*32 > 0) else 0 for i in range(8)]
        print(led_vals)

        GPIO.output(leds, led_vals)
       

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()