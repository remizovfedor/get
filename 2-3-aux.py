import RPi.GPIO as GPIO
import time

# leds = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2,   3,  4, 17, 27, 22, 10,  9]
aux  = [24, 23, 25, 19, 16, 26, 20, 21]

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

GPIO.setup(aux , GPIO.IN)
GPIO.setup(leds, GPIO.OUT)


while 1:
    for i in range(8):
        GPIO.output(leds[i], GPIO.input(aux[i]))

GPIO.cleanup()