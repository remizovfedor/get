import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

dac = [8, 11, 7, 1, 0, 5, 12, 6]
numbers = [255, 127, 64, 32, 5, 0, 256]
voltages = []

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

for num in numbers:
    print("current num: ",num)
    bin_num = numberToBin(num)
    GPIO.output(dac, bin_num)
    
    voltages.append(float(input()))

print(voltages)

# plt.plot(numbers, voltages)
# plt.show


GPIO.output(dac, 0)

GPIO.cleanup()