import pigpio
import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('Agg')
pi = pigpio.pi()

if not pi.connected:
    print("no pi")
    exit()

bus = 1
address = 0x5a
read_bytes = 1



handle = pi.i2c_open(bus,address)


b=[]
for i in range(0,50):

    count, data = pi.i2c_read_device(handle, read_bytes)
    time.sleep(0.5)



    print(count)


    a=[float(x) for x in data]
    print(a)
    b.append(a[0])

print(b)
plt.plot(b)
