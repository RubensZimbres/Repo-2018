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
Copy key code and paste into Ubuntu One:  

```
ssh-rsa ABCDEF12345ABCDEF12345ABCDEF12345ABCDEF12345ABCDEF12345ABCDEF12345ABCDEF12345ABCDEF12345ABCDEF12345ABCDEF12345ABCDEF12345 user@Dell
```

Turn on Raspberry:

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/raspberry_OK%20(1).png>  

Configure network and setup administrator account connected to Ubuntu One. SSH into your Raspberry. 

```
sudo apt-get install openssh-server
sudo ufw allow 22
sudo service ssh start
ssh your_user@191.168.15.XXX
```  

```
ssh-keygen -R 192.168.15.XXX
cd .ssh
rm *
cp id_rsa ~/.ssh/id_rsa
cp id_rsa.pub ~/.ssh/id_rsa.pub
ssh your_user@191.168.15.XXX
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
CTRL+C   INSERT    CTRL+SHIFT+V  
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

```
source .bashrc
sudo python LED.py
 ```  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/LED_22.png>  

<b>4 - Save data in Dynamo DB</b>  

<b>5 - Add LM 35 Temperature Sensor</b>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20IoT-Project/Pictures/LM35_sensor.png>

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
(sudo python setup.py install)
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

References:  
https://www.totalphase.com/support/articles/200349176-7-bit-8-bit-and-10-bit-I2C-Slave-Addressing  
https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial  

To do:  
* w1thermsensor - code.py + digital temperature sensor
* gpio -g ... (get base address)


<b>6 - Load trained Machine Learning model</b>  

<b>7 - Dashboard</b>  

ShutDown:
```
sudo shutdown now -h
```  
