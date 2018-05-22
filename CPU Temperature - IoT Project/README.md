# IoT Project - CPU Temperature from Ubuntu to AWS IoT  

Google Colab has open source projects that help Data Scientists everywhere. Inspired in this mindset, I developed my first IoT project using my notebook as an IoT device and AWS IoT as infrastructure. Recently I bought a Raspberry Pi, but it didn't arrive yet.

So, I had a "simple" idea: collect CPU Temperature from my Notebook running on Ubuntu, send to Amazon AWS IoT, save data, make it available for Machine Learning models and dashboards.

However, the operationalization of this idea is quite complex: first, develop a Python notebook that runs Ubuntu command line internally ('sensors'), collecting CPU temperature and is able to connect to AWS IoT via proper security protocols using MQTT.

It is necessary to create a Thing at AWS IoT, get the Certificates, create and attach the Policy and create a SQL Rule to send data (JSON) to Cloud Watch and Dynamo DB. Then, create a Data Pipeline from Dynamo DB to S3, so that the data become available for a Machine Learning model and also to AWS Quick Sight dashboard.

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

<b> Open ports  </b>  

```
sudo ufw allow 8443
sudo ufw allow 8883
```

<b> Set Up Amazon AWS IoT </b>  

Device shadow:  

```
{
  "desired": {
    "light": "green",
    "Temperature": "55",
    "timestamp": 1526323886
  },
  "reported": {
    "light": "blue",
    "Temperature": "55",
    "timestamp": 1526323886
  },
  "delta": {
    "light": "green"
  }
}

```

<b>Create certificate and CA:</b>  

<b>Log in into AWS IoT</b>  

```
python AWS_Send_test2BEST_QUASE4.py -e a2th12345.iot.us-east-1.amazonaws.com -r rootCA.pem -c 2733c12345-certificate.pem.crt -k 2722c12345-private.pem.key -id arn:aws:iot:us-east-1:1391112345:thing/CPUUbuntu -t 'Teste'

```  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CPU%20Temperature%20-%20IoT%20Project/Pictures/Success_Connect.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CPU%20Temperature%20-%20IoT%20Project/Pictures/Messages_.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CPU%20Temperature%20-%20IoT%20Project/Pictures/Shadow_Update_.png>  

<b>Create SQL query + rule to Dynamo:</b>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CPU%20Temperature%20-%20IoT%20Project/Pictures/Best1_Dynamo.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CPU%20Temperature%20-%20IoT%20Project/Pictures/Best2_Dynamo.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CPU%20Temperature%20-%20IoT%20Project/Pictures/Best3_Dynamo.png>  

<b>Create Dashboards in CloudWatch:</b>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CPU%20Temperature%20-%20IoT%20Project/Pictures/AWS_Git_.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CPU%20Temperature%20-%20IoT%20Project/Pictures/Cloud_Watch_Git2.png>

<b>Create Data Pipeline from DynamoDB to S3 to be ingested by QuickSight</b>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CPU%20Temperature%20-%20IoT%20Project/Pictures/Pipeline.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CPU%20Temperature%20-%20IoT%20Project/Pictures/DataPipelineCondig.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CPU%20Temperature%20-%20IoT%20Project/Pictures/data.png>

<b>Visualize Telemetry data with Quick Sight</b>  

Edit S3 import JSON in Quick Sight:  

```
{
    "fileLocations": [
        {
            "URIs": [
                "https://s3.amazonaws.com/your-bucket2/2018-05-20-12-32-49/12345-a279-1243-b269-12345"
            ]
        },
        {
            "URIPrefixes": [
                "https://s3.amazonaws.com/your-bucket2/2018-05-20-12-32-49/12345-a279-1243-b269-12345"
            ]
        }
    ],"globalUploadSettings": {"format":"JSON",
        "delimiter":"\n","textqualifier":"'"
    }
}
```

<b>Import data and Generate Plot with AWS Quick Sight</b>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CPU%20Temperature%20-%20IoT%20Project/Pictures/Quick_Sight_OK.png>

And it's done ...  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CPU%20Temperature%20-%20IoT%20Project/Pictures/ProjectFINAL.png>

<b>Run an Athena Query:</b>  

```
CREATE EXTERNAL TABLE IF NOT EXISTS S3.S3 (
  `Temperature` float,
  `light` string,
  `timestamp` int 
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = '1'
) LOCATION 's3://your-bucket/2018-05-20-12-32-49/'
TBLPROPERTIES ('has_encrypted_data'='false');
```
