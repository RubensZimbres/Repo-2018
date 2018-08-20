from Adafruit_ADS1x15 import ADS1x15
from time import sleep
import math, signal, sys, os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

delayTime = 0.5

ADS1015 = 0x00  # 12-bit ADC
ADS1115 = 0x01  # 16-bit

gain = 4096  # +/- 4.096V
sps = 64   # 64 Samples per second

adc_channel_0 = 0    # Channel 0
adc_channel_1 = 1    # Channel 1
adc_channel_2 = 2    # Channel 2
adc_channel_3 = 3    # Channel 3

# ERROR HERE
adc = ADS1x15(ic=ADS1115)

Digital_PIN = 8
GPIO.setup(Digital_PIN, GPIO.IN, pull_up_down = GPIO.PUD_OFF)
 
 
try:
        while True:
                #Current values will be recorded
                analog = adc.readADCSingleEnded(adc_channel_0, gain, sps)
 
                # Output at the terminal
                if GPIO.input(Digital_PIN) == False:
                        print("Analog voltage value:", analog,"mV, ","extreme value: not reached")
                else:
                        print("Analog voltage value:", analog, "mV, ", "extreme value: reached")
                print("---------------------------------------")
 
                sleep(delayTime)
 
 
 
except KeyboardInterrupt:
        GPIO.cleanup()
