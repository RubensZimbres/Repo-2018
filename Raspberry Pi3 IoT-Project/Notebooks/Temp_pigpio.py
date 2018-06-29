import time
import pigpio

pi = pigpio.pi()

pi.set_mode(7, pigpio.INPUT)

while True:
  print(float(pi.read(7)))
  time.sleep(1)

pi.stop()
