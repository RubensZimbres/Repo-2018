# Raspberry Pi3 Model B for IoT Project - Ubuntu Core  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry-Pi3-IoT-Project/Pictures/Raspberry_run.png>  

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

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry-Pi3-IoT-Project/Pictures/raspberry_OK%20(1).png>  

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


<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry-Pi3-IoT-Project/Pictures/temp_run.png>

<b>4 - Send Data to AWS</b>  

<b>4 - Save data into Dynamo DB</b>  

<b>5 - Add sensor</b>  

<b>6 - Load saved Machine Learning model for anomaly detection</b>  

<b>7 - Dashboard</b>  
