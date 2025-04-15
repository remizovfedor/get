import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
period_in_sec = 10

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def dec2bin(num):
    bin_number = [0 for i in range(8)]
    d_num = num % 256
    bin_num = bin(d_num)

    i = -1
    while bin_num[i] != 'b':
        bin_number[i] = int(bin_num[i])
        i -= 1

    return bin_number

try:
    while 1:
        for i in range(0, 256):
            GPIO.output(dac, dec2bin(i))
            time.sleep(period_in_sec / (2 * 256))

        for i in range(255, -1, -1):
            GPIO.output(dac, dec2bin(i))
            time.sleep(period_in_sec / (2 * 256))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()