# Raspberry Pi3 Model B for IoT Project - Ubuntu Core  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/Core_logo.png> <img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/Raspberry_logo.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/Raspberry_run.png>  

<b>1 - Plug and Play</b>  

Open "Disks" and find path to SDCard.  
Download Ubuntu Core Image: http://cdimage.ubuntu.com/ubuntu-core/16/stable/current/ubuntu-core-16-pi3.img.xz  
Flash it with Etcher to SDCard: https://etcher.io/  

Insert SDCard into Raspberry.  

Back to your computer, generate private and public key.

```
mkdir ~/.ssh
chmod 700 ~/.ssh
ssh-keygen -t rsa -b 4096
```  
Copy key code and Upload to your Ubuntu One account:  

```
ssh-rsa ABCDEF12345ABCDEF12345ABCDEF12345ABCDEF12345ABCDEF12345ABCDEF12345ABCDEF12345ABCDEF12345ABCDEF12345ABCDEF12345ABCDEF12345 user@Dell
```

Turn on Raspberry:

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/raspberry_OK%20(1).png>  

Configure network and setup administrator account connected to Ubuntu One. SSH into your Raspberry. 

```
sudo ufw allow 22
sudo service ssh start
```  

```
ssh-keygen -R 192.168.15.XXX
mkdir .ssh
cp id_rsa ~/.ssh/id_rsa
cp id_rsa.pub ~/.ssh/id_rsa.pub
cd .ssh
rubens@dell:~/.ssh$  ssh your_user@192.168.15.XXX (OR)
rubens@dell:~/.ssh$  ssh 192.168.15.XXX -l rubens
```  

```
ifconfig
route -n
```

Your login will change:
```
rubens@localhost:~$
```  

You're in ! Install snap classic.  

```
sudo snap install classic --edge --devmode
sudo classic

Creating classic environment
Parallel unsquashfs: Using 4 processors
11111 inodes (11975 blocks) to write

[===========================================================/] 11975/11975 100%

(classic)rubens@localhost:~$ sudo apt update
sudo apt install snapcraft build-essential git
```

<b>2 - Collect CPU Temperature and Connect Raspberry to AWS IoT</b>  

```
import shlex
import subprocess
def measure_temp():
        temp = subprocess.Popen(shlex.split('sensors'),
                                stdout=subprocess.PIPE,
                                bufsize=10, universal_newlines=True)
        return temp.communicate()[0]
```  

```
export LC_ALL=C
source .bashrc
pip install setuptools
pip install AWSIoTPythonSDK
```  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/temp_run.png>

Create a blank file, copy and paste contents of AWS_Send_0.py via vim, then ESC:wq ENTER:  

```
touch AWS_Send_0.py
vi AWS_Send_0.py
```

```
python AWS_Send_0.py -e a23312345.iot.us-east-1.amazonaws.com -r rootCA.pem -c 123412345-certificate.pem.crt -k 12345-private.pem.key -id arn:aws:iot:us-east-1:1123112345:thing/CPUUbuntu -t 'Teste'
```  

Now you can ping AwS IoT Core:  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/AWS_Raspberry.png>  

Copy certificates to your Raspberry:  

```
lsblk

NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda           8:0    1  58.2G  0 disk 
`-sda1        8:1    1    32G  0 part 
loop0         7:0    0  70.9M  0 loop /snappy
loop1         7:1    0  85.6M  0 loop 
loop2         7:2    0  70.9M  1 loop 
loop3         7:3    0  85.6M  1 loop 
loop4         7:4    0   5.9M  1 loop 
loop5         7:5    0  73.4M  1 loop 
loop6         7:6    0 128.8M  1 loop 
loop7         7:7    0     4K  1 loop 
mmcblk0     179:0    0   7.4G  0 disk 
|-mmcblk0p1 179:1    0   128M  0 part 
`-mmcblk0p2 179:2    0   7.3G  0 part /home

sudo mkdir /mnt/usb
sudo mount /dev/sda1 /mnt/usb
sudo cp /mnt/usb/27aa12345-public.pem.key 27aa12345-public.pem.key
```  
Remember to copy rootCA.pem + *.crt + *private.pem.key + *.public.pem.key

<b>4 - Send Data to AWS</b>  

Run AWS_Send_0.py at rubens@localhost:~$

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/AWS_running_Raspberry.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/Raspberry_AWS_Success.png>  

<b>Let's Blink a LED:</b>

```
sudo pip install setuptools
sudo pip install wheel
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-pip python-dev
sudo pip install RPi.GPIO
sudo chown rubens /dev/gpiomem
sudo chmod g+rw /dev/gpiomem
```  
Connect LED and 2 resistors (4.7 Ohms) in parallel using wires:  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/GPIO_OK.png>  

https://pinout.xyz/pinout/pin7_gpio4  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/map_LED.png>  

Develop LED.py  
```
touch LED.py
vi LED.py
```  
CTRL+C   i  i     CTRL+SHIFT+V  
```
import RPi.GPIO as GPIO 
from time import sleep 

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) 

while True: 
    GPIO.output(8, GPIO.HIGH) 
    sleep(1) 
    GPIO.output(8, GPIO.LOW) 
    sleep(1) 
```  
ESC : w q

```
source .bashrc
sudo python LED.py
 ```  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/blink_LED.png>  

<b>4 - Save data in Dynamo DB</b>  


```
sudo vi /etc/modules
#add
w1-gpio
w1-therm
i2c-dev

sudo vi /boot/config.txt
#add 
device_tree=bcm2708-rpi-b.dtb 
device_tree_overlay=overlays/w1-gpio-overlay.dtb
dtoverlay=w1-gpio,gpiopin=7
dtparam=i2c_arm=on

sudo vi /etc/environment
#add
export W1THERMSENSOR_NO_KERNEL_MODULE=1
W1THERMSENSOR_NO_KERNEL_MODULE=1 python Temp.py

#Reboot

pip install w1thermsensor OR
pip install --index-url=https://pypi.python.org/simple/ w1thermsensor

sudo apt-get install -y i2c-tools
sudo adduser rubens i2c
#Reboot

sudo i2cdetect -y 1
sudo i2cdetect -l

```  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/i2c_detect_empty.png> 

Check GPIOs.  

```
git clone git://git.drogon.net/wiringPi
cd ~/wiringPi
git pull origin
./build
gpio readall
```  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/GPIO_Readall.png>

Connect sensor.

```
sudo lsmod

Module                  Size  Used by
nls_ascii              16384  1
joydev                 20480  0
hid_generic            16384  0
brcmfmac              282624  0
brcmutil               20480  1 brcmfmac
usbhid                 57344  0
cfg80211              557056  1 brcmfmac
hid                   114688  2 hid_generic,usbhid
i2c_bcm2708            16384  0
bcm2835_wdt            16384  0
bcm2835_gpiomem        16384  0
uio_pdrv_genirq        16384  0
uio                    20480  1 uio_pdrv_genirq

sudo python Temp_read_GPIO.py
```  
Install pigpio:  

```
sudo apt-get install wget
sudo apt-get install unzip
wget https://github.com/joan2937/pigpio/archive/master.zip
unzip master.zip
cd pigpio-master
make
sudo make install

sudo pigpiod
pigs r 7

(classic)rubens@localhost:~/pigpio-master$ python3 Temp_pipio.py

```  

```
export LC_ALL=C
source .bashrc
sudo pip install smbus2

sudo i2cdetect -y 1

sudo python Temp_smbus.py
```  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/pin_mappings_MS.png>

References:  
https://www.totalphase.com/support/articles/200349176-7-bit-8-bit-and-10-bit-I2C-Slave-Addressing  
https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/diagram_circuits.png>  

```
export LC_ALL=C
source .bashrc

wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh
sudo md5sum Miniconda3-latest-Linux-armv7l.sh
sudo /bin/bash Miniconda3-latest-Linux-armv7l.sh
sudo reboot -h now

export LC_ALL=C
sudo chmod -R a+rX /home/rubenszmm/miniconda3
sudo chown -R rubenszmm /home/rubenszmm/miniconda3
conda install scikit-learn

(Careful)
sudo vi /etc/dphys-swapfile
CONF_SWAPSIZE=1024

sudo apt-get install python3-numpy
sudo apt-get install libblas-dev
sudo apt-get install liblapack-dev
sudo apt-get install python3-dev 
sudo apt-get install libatlas-base-dev
sudo apt-get install gfortran
sudo apt-get install python3-setuptools
sudo apt-get install python3-scipy
sudo apt-get update
sudo apt-get install python3-h5py
 
wget https://github.com/lhelontra/tensorflow-on-arm/releases/download/v1.8.0/tensorflow-1.8.0-cp35-none-linux_armv7l.whl
```  

These steps below will take one hour or longer:  

```
(classic)rubens@localhost:~/miniconda3$ 

sudo apt-get install python-software-properties
conda install anaconda-client

cp /home/rubens/tensorflow-1.8.0-cp35-none-linux_armv7l.whl tensorflow-1.8.0-cp35-none-linux_armv7l.whl
easy_install pip==1.5.6 (8.1.1)
pip install numpy==1.14.5
sudo apt-get install python3-pip
sudo pip3 install tensorflow-1.8.0-cp35-none-linux_armv7l.whl

sudo pip3 install keras 

sudo python3

sudo apt-get install software-properties-common
sudo apt-get install libstdc++6
sudo add-apt-repository ppa:ubuntu-toolchain-r/test 
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade
```  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/keras_raspberry_success.png>  

```
sudo apt-get install gcc-arm-linux-gnueabihf

git clone https://github.com/adafruit/Adafruit_Python_DHT
cd Adafruit_Python_DHT
sudo python setup.py install

export LC_ALL=C (pip3)
source .bashrc
sudo pip3 install spidev

sudo apt-get install pkg-config

sudo apt-get install libfreetype6-dev
sudo apt-get install bedtools

sudo apt-get install python3-matplotlib
sudo apt-get install python-tk
sudo apt-get install libgtk-3-dev
sudo apt-get update

sudo pip3 install pycairo
wget https://files.pythonhosted.org/packages/e0/e8/1e4f21800015a9ca153969e85fc29f7962f8f82fc5dbc1ecbdeb9dc54c75/PyGObject-3.28.3.tar.gz
tar -xvzf PyGObject-3.28.3.tar.gz
cd PyGObject-3.28.3
sudo python setup.py install
sudo apt-get install tcl-dev tk-dev python-tk python3-tk

sudo vi ~/.ssh/config
Add:
ForwardX11 yes

Reboot
```

Everything installed at sudo python3. Here OK:

```
rubens@localhost:~$ sudo classic
(classic)rubenszmm@localhost:~$ sudo python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import keras
Using TensorFlow backend.
>>> import matplotlib
>>> 
```

```
(classic)rubens@localhost:~/pigpio-master$ sudo pigpiod
(classic)rubens@localhost:~/pigpio-master$ sudo python3 Temp_pipio.py
```  


<b>5 - Add Micro Sound Sensor on i2c SDA on pin 3: Adjust potentiometer for i2cdetect: </b>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/i2c-detect_ok.png>  

Use Temp_pigpio*.py

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/temp_character.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/hex_temp.png>  

```
sudo killall pigpiod
sudo pigpiod

sudo apt-get install man
cd wiringPi
man gpio
gpio -g mode 7 input

cd pigpio-master
wget http://abyz.me.uk/rpi/pigpio/code/gpiotest.zip
unzip gpiotest.zip
sudo pigpiod
bash gpiotest

Testing...
Skipped non-user gpios: 0 1 28 29 30 31 
Tested user gpios: 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 
Failed user gpios: None

```

<b>Buzzer KY-012:</b>  

```
KY-012	Raspberry
S	Pin 7
-	GND
```  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/buzzer.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/serial_buzzer_2.png>  
<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/small_kit.png>  


<b>Big Sound Detector + Laser Beam + LED:</b>  

Be sure to adjust potentiometer.  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/big_sound.png>  


```
sudo i2cdetect -y 1

Example:
0x00 - bx50 connected
```  


```
sudo i2cget -y 1 0x20
sudo python3 pigpio1.py

import pigpio
import time
pi=pigpio.pi()
while True:
    (b,d)=pi.i2c_read_block_data(0x20,(3))
    print(b)
    print(d)
    time.sleep(1)

gpio -g mode 3 input
sudo i2cdetect -y 1
```  

```
wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.56.tar.gz
cd bcm2835-1.56
./configure
make
sudo make check
sudo make install

cd Adafruit_Python_DHT
sudo python setup.py install

(classic)rubens@localhost:~/Adafruit_Python_DHT/examples$ sudo python Adafruit_DHT.py 11 8

```  
<b>Touch sensor + LED + Buzzer:</b>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/Touch_sensor.png>  

<b>Air Conditioning Control + Shut Off Computer:</b>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/air_conditioning_off.png>

```
PROBLEMS:
sudo apt-get install kmod
1 - sudo modprobe i2c-dev
2 - i2cdetect ALL APPEAR
```
```
sudo vi /etc/group file.
Add:
wheel:x:10:root
ESC:w !sudo tee %

sudo vi /etc/sudoers
Add:
%wheel ALL= NOPASSWD: /sbin/shutdown
ESC:wq!
ESC:w !sudo tee %
ENTER "O"  (oh)
:q!

sudo -i
which python
cd miniconda3
sudo /home/rubenszmm/miniconda3/bin/python3 /home/rubenszmm/shutdown.py
```  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/DHT11%E2%80%93Temperature-Sensor-Pinout.jpg>

To do:  

* DY-028  

* RGB Iris sklearn  

* temperature sensor DHT11  

* Advantech  

* w1thermsensor - code.py + digital temperature sensor -- DS18B20  

* movidius  


<b>6 - Load trained Machine Learning model</b>  

<b>7 - Dashboard</b>  

ShutDown:
```
sudo shutdown now -h
```  
