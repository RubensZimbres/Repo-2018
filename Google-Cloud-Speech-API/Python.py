## ENVIRONMENT VARIABLE -- GOOGLE_APPLICATION_CREDENTIALS="D:\VM\Google Cloud\Speech_API_123456789.json"

import time
start=time.time()

import io
import os

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

#! pip install --upgrade google-cloud-storage
#! pip install webapp2
#! pip install cloudstorage
#! pip install GoogleAppEngineCloudStorageClient

from google.cloud import storage

client = storage.Client()

bucket = client.get_bucket('storagexxx')

blob = bucket.get_blob('Info/1-NotSolved_No_Silence.wav')

blob3=blob.upload_from_filename(filename='1-NotSolved_No_Silence.wav')  


audio = types.RecognitionAudio(content=blob3)


client = speech.SpeechClient()

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.MULAW,
    sample_rate_hertz=8000,enable_word_time_offsets= False,
    language_code='pt-BR',
    enable_automatic_punctuation= False,
    use_enhanced=True)

audio=types.RecognitionAudio(uri="gs://storagexxx/Info/1-NotSolved_No_Silence.wav")

operation = client.long_running_recognize(config, audio)

print('Waiting for operation to complete...')
response = operation.result(timeout=90)
response

for result in response.results:
        print(u'Transcript: {}'.format(result.alternatives[0].transcript))
        print('Confidence: {}'.format(result.alternatives[0].confidence))
end=time.time()

print((end-start)/60,'minutos')
