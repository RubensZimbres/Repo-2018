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
    if GPIO.input(5)==GPIO.LOW:
        GPIO.output(7, GPIO.HIGH)
        sleep(1)
        os.system("ssh rubenszmm@192.168.15.32")
        time.sleep(8)
        os.system("sudo shutdown -r now")
    else:
        sleep(1)
        GPIO.output(7, GPIO.LOW)
