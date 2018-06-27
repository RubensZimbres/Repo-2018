import time
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()
while True:
    temperature = sensor.get_temperature()
    print(temperature)
    time.sleep(1)
