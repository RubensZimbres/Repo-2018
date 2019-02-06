from __future__ import print_function
import time
import boto3
transcribe = boto3.client('transcribe')
job_name = "Name4"
job_uri = "https://s3.amazonaws.com/bucket/Inform_Clean2.wav"
transcribe.start_transcription_job(
    TranscriptionJobName=job_name,
    Media={'MediaFileUri': job_uri},
    MediaFormat='wav',
    LanguageCode='pt-BR',
    OutputBucketName= "cdf-ok",
    MediaSampleRateHertz=8000,
    Settings={"MaxSpeakerLabels": 2,
      "ShowSpeakerLabels": True})

while True:
    status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
    print('Not ready yet')
    time.sleep(15)
print(status)

import json

s3=boto3.client('s3')

obj = s3.get_object(Bucket='cdf-ok', Key=job_name+'.json')
j = json.loads(obj['Body'].read())

print(j)

a1=[]
for i in range(0,len(j['results']['speaker_labels']['segments'])):
    for k in range(0,len(j['results']['speaker_labels']['segments'][i]['items'])):
        a1.append(j['results']['speaker_labels']['segments'][i]['items'][k]['speaker_label'][4:5])

b1=[]
for i in range(0,len(j['results']['items'])):
    for k in range(0,len(j['results']['items'][i]['alternatives'])):
        b1.append(j['results']['items'][i]['alternatives'][k]['content'])

len(a1)

len(b1)

len([word.lower() for word in b1 if word.isalpha()])

import numpy as np

np.array([word.lower() for word in b1 if word.isalpha()])[np.where(np.array(a1)=='0')[0]]

np.array([word.lower() for word in b1 if word.isalpha()])[np.where(np.array(a1)=='1')[0]]
