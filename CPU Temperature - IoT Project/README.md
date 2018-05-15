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
    time.sleep(5)
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
start=time.time()
    
while True:
    args.message={"desired": {"light": "green","Temperature": 55.22,
                              "timestamp": 1526323886},
    "reported": {"light": "blue","Temperature": measure_temp()[0].split()[8],"timestamp": time.time()
    },"delta": {"light": "green","Temperature": time.time()-start}}
    print(measure_temp()[0].split()[8])
    time.sleep(5)

```  

Remove 'message' from arguments  in shell.  

<b> Install program sensors in Ubuntu </b> 

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
Log in into AWS IoT  

```
python AWS_Send_test.py -e 12345.iot.us-east-1.amazonaws.com -r CA_Raiz.txt -c 12345-certificate.pem.crt -k 12345-private.pem.key -id arn:aws:iot:us-east-1:12345:thing/CPU-Ubuntu -t Politica-Rubens
```  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CPU%20Temperature%20-%20IoT%20Project/Pictures/IoT_.png>

Create rule to DynamoDB:  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CPU%20Temperature%20-%20IoT%20Project/Pictures/DynamoDB.png>  
Save data to DynamoDB:   

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CPU%20Temperature%20-%20IoT%20Project/Pictures/DynamoDB_.png>

Create rule to Lambda:  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CPU%20Temperature%20-%20IoT%20Project/Pictures/Lambda.png>

Visualize Telemetry data:  
