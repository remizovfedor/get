import RPi.GPIO as GPIO
import time

pwm_pin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_pin, GPIO.OUT)

pwm = GPIO.PWM(pwm_pin, 1000)
pwm.start(0)

try:
    while 1:
        f = int(input("Enter number 0-100: "))
        pwm.ChangeDutyCycle(f)
        print("Expected: ", 3.3 * f / 100)

finally:
    pwm.stop()
    GPIO.output(pwm_pin, 0)
    GPIO.cleanup()