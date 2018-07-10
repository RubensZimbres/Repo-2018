#!/usr/bin/env python

import time

import pigpio # http://abyz.co.uk/rpi/pigpio/python.html

# DS18B20-1.py
# 2016-06-29
# Public Domain

"""
This uses the file interface to access the remote file system.

In this case it is used to access the sysfs 1-wire bus interface
to read any connected DS18B20 temperature sensors.

The remote file /opt/pigpio/access is used to grant access to
the remote file system.

For this example the file must contain the following line which
grants read access to DS18B20 device files.

/sys/bus/w1/devices/28*/w1_slave r
"""
pi = pigpio.pi()

if not pi.connected:
   exit()

while True:

   """
   Get list of connected sensors, handle error rather than the
   default of raising exception if none found.
   """

   pigpio.exceptions = False
   c, files = pi.file_list("/sys/bus/w1/devices/28-00*/w1_slave")
   pigpio.exceptions = True

   if c >= 0:

      for sensor in files[:-1].split("\n"):

         """
         Typical file name

         /sys/bus/w1/devices/28-000005d34cd2/w1_slave
         """

         devid = sensor.split("/")[5] # Fifth field is the device Id.

         h = pi.file_open(sensor, pigpio.FILE_READ)
         c, data = pi.file_read(h, 1000) # 1000 is plenty to read full file.
         pi.file_close(h)

         """
         Typical file contents

         73 01 4b 46 7f ff 0d 10 41 : crc=41 YES
         73 01 4b 46 7f ff 0d 10 41 t=23187
         """

         if "YES" in data:
            (discard, sep, reading) = data.partition(' t=')
            t = float(reading) / 1000.0
            print("{} {:.1f}".format(devid, t))
         else:
            print("999.9")

   time.sleep(3.0)
