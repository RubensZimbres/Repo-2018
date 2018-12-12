import requests

KERAS_REST_API_URL = "http://localhost:5000"
IMAGE_PATH = "dog.jpg"

image = open(IMAGE_PATH, "rb").read()
payload = {"image": image}

r = requests.post(KERAS_REST_API_URL, files=payload).json()

print(r)
