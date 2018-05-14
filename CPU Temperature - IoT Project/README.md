# IoT Project - CPU Temperature from Ubuntu to AWS IoT  

<b> Create .py file to collect CPU Temperature in Ubuntu </b>  

```
import subprocess
import shlex
import time

def measure_temp():
        temp = subprocess.Popen(shlex.split('sensors -u'),
                                stdout=subprocess.PIPE,
                                bufsize=10, universal_newlines=True)
        return temp.communicate()
    
while True:
    string=measure_temp()[0]
    print(string.split()[8])
    time.sleep(2)
```  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CPU%20Temperature%20-%20IoT%20Project/Pictures/Notebook_IoT.png>

<b> Edit basicPubSub.py from AWS library (AWSIoTPythonSDK) to communicate data to AWS IoT</b>  

Add:  

```
def measure_temp():
        temp = subprocess.Popen(shlex.split('sensors -u'),
                                stdout=subprocess.PIPE,
                                bufsize=10, universal_newlines=True)
        return temp.communicate()
    
while True:
    args.message=measure_temp()[0]
```  

Remove 'message' from arguments  in notebook.  

<b> Install sensors in Ubuntu </b> 

```
sudo apt-get install lm-sensors
sudo service kmod start
```

<b> Open port  </b>  

```
sudo ufw allow 8443
```

<b> Set Up Amazon AWS IoT </b>  

Device shadow:  

```
{
  "desired": {
    "light": "green",
    "Temperature": 55
  },
  "reported": {
    "light": "blue",
    "Temperature": 65
  },
  "delta": {
    "light": "green",
    "Temperature": 55
  }
}
```  

```
python AWS_Send_test.py -e 12345.iot.us-east-1.amazonaws.com -r CA_Raiz.txt -c 12345-certificate.pem.crt -k 12345-private.pem.key -id arn:aws:iot:us-east-1:12345:thing/CPU-Ubuntu -t Temperature
```  


