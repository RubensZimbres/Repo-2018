import requests

KERAS_REST_API_URL = "http://your_beanstalk_API_address.us-west-1.elasticbeanstalk.com"
IMAGE_PATH = "dog.jpg"

image = open(IMAGE_PATH, "rb").read()
payload = {"image": image}

r = requests.post(KERAS_REST_API_URL, files=payload).json()

print(r)
