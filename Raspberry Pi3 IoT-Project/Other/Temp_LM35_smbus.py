# RaspEasy7c.py
# LM35 temperature sensor

import smbus
import time
#from OLED1306 import OLED1306

bus = smbus.SMBus(1)

def readData(port = 0):
    if port == 0:
        adc_address = 0x48
    elif port == 1:    
        adc_address = 0x4D
    rd = bus.read_word_data(adc_address, 0)
    data = ((rd & 0xFF) << 8) | ((rd & 0xFF00) >> 8)
    data = data >> 2
    return data

print("starting...")
#oled = OLED1306()
#oled.setFontSize(50)

bus = smbus.SMBus(1) 
while True:
    v = readData()
    T = v / 3.1
    print("T = %4.1f centigrades" %T)
#    oled.setText(str(int(T + 0.5))) # rounded to int
    time.sleep(1)
