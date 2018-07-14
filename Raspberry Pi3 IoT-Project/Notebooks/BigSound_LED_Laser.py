import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(8,GPIO.IN)
while True:
    if GPIO.input(8)==GPIO.LOW:
        GPIO.output(7, GPIO.HIGH)
        sleep(1)
    else:
        sleep(1)
        GPIO.output(7, GPIO.LOW)
    
