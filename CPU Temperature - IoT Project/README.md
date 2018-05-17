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

<b> Install program sensors in Ubuntu and AWSIoTPythonSDK library </b> 

```
sudo apt-get install lm-sensors
sudo service kmod start  

pip install AWSIoTPythonSDK
```

<b> Check CPU Temperature  </b>  

```
sensors
```  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CPU%20Temperature%20-%20IoT%20Project/Pictures/sensors2.png>  

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
    "Temperature": "55.22",
    "timestamp": 1526323886
  },
  "reported": {
    "light": "blue",
    "Temperature": "55.22",
    "timestamp": 1526323886
  },
  "delta": {
    "light": "green"
  }
}

```

<b>Log in into AWS IoT</b>  

```
python AWS_Send_test.py -e a2thz12345.iot.us-east-1.amazonaws.com -r CA_Raiz.txt -c 6612345-certificate.pem.crt -k 6612345-private.pem.key -id arn:aws:iot:us-east-1:1391112345:thing/CPU-Ubuntu -t '#'
```  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CPU%20Temperature%20-%20IoT%20Project/Pictures/IoT_.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CPU%20Temperature%20-%20IoT%20Project/Pictures/Shadow_Update_.png>  

<b>Create SQL query + rule to S3:</b>  

```
SELECT * FROM '#'
```

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CPU%20Temperature%20-%20IoT%20Project/Pictures/S3_bucket.png>    
<b>Create Dashboards in CloudWatch:</b>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CPU%20Temperature%20-%20IoT%20Project/Pictures/Cloud_Watch_Git2.png>

<b>Visualize Telemetry data:</b>  

Almost ready ...  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CPU%20Temperature%20-%20IoT%20Project/Pictures/AWS_IoT_PPT_4.png>
