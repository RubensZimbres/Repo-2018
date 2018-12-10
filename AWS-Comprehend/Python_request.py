import boto3
import json

comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
text = "Damn it! It is raining 30 milimeters today in Los Angeles!"

print('Calling DetectEntities')
print(json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
print(json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
