# Raspberry Pi3 Model B for IoT Project - Ubuntu Core

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

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Raspberry%20Pi3%20B%20-%20IoT%20Project/Pictures/raspberry_OK.png>  

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
(classic)rubens@localhost:~$
```



<b>2 - Set up Amazon AWS IoT</b>  

<b>3 - Collect CPU Temperature and Connect Raspberry to AWS IoT</b>  

```
from subprocess import PIPE, Popen

def get_cpu_temperature():
    """get cpu temperature using vcgencmd"""
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
    output, _error = process.communicate()
    return float(output[output.index('=') + 1:output.rindex("'")])
```

<b>7 - Save data into Dynamo DB</b>  

<b>8 - Add sensor</b>  

<b>9 - Load saved Machine Learning model for anomaly detection</b>  

<b>10 - Dashboard</b>  
