import requests
import boto3
from io import BytesIO
import matplotlib.image as mpimg

client = boto3.client('s3')

resource = boto3.resource('s3')
my_bucket = resource.Bucket('bucket-vecto')

image_object = my_bucket.Object('dog.jpg')
image = mpimg.imread(BytesIO(image_object.get()['Body'].read()), 'jpg')

KERAS_REST_API_URL = "http://localhost:5000/predict"

payload = {"image": image}

r = requests.post(KERAS_REST_API_URL, files=payload)

#.json()

print(r.content)

if r["success"]:
    for (i, result) in enumerate(r["predictions"]):
        print("{}. {}: {:.4f}".format(i + 1, result["label"],
            result["probability"]))
else:
    print("Request failed")
