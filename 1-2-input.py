import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)
GPIO.setup(22, GPIO.IN)

GPIO.output(14, GPIO.input(22))