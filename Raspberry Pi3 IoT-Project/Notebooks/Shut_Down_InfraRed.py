import os
import RPi.GPIO as GPIO
from time import sleep
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(5,GPIO.IN)
while True:
    print(GPIO.input(5))
    if GPIO.input(5)==GPIO.HIGH:
        GPIO.output(7, GPIO.HIGH)
        sleep(1)

        time.sleep(8)

        os.system("exit && sudo poweroff -f")
    else:
        sleep(1)

        GPIO.output(7, GPIO.LOW)

