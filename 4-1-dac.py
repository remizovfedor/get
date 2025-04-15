import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def numberToBin(num):
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
        str = input("Enter the number (0-255): ")

        try:
            num = int(str)

            if 0 <= num <= 255:
                dac_out = numberToBin(num)
                print("Expexted: ", 3.3 * num / 255 , "V")
                GPIO.output(dac, dac_out)
            else:
                if num < 0:
                    print("Needs to be >= 0")
                elif num > 255:
                    print("Too much")
        except Exception:
            if str == "q": break
            print("only int numbers!!!")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()