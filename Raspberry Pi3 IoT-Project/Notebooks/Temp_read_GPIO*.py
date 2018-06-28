import RPi.GPIO as GPIO 
from time import sleep 

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(7, GPIO.IN) 

while True: 
    print(float(GPIO.input(7)) 
    sleep(1)
