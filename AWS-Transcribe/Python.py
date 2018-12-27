from __future__ import print_function
import time
import boto3

transcribe = boto3.client('transcribe')
job_name = "Name"
job_uri = "https://s3.amazonaws.com/bucket/Inform_Clean.wav"

transcribe.start_transcription_job(
    TranscriptionJobName=job_name,
    Media={'MediaFileUri': job_uri},
    MediaFormat='wav',
    LanguageCode='pt-BR')

while True:
    status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
    print('Not ready yet')
    time.sleep(15)
print(status)
