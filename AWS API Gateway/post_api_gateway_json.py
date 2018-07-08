import requests
import json
API_URL = "https://abcd1234.execute-api.us-east-1.amazonaws.com/stage"

message ={"TableName":"Sensor","Item":{"type":{"S":"22"},"page":{"S":"2"}}}

headers = {'content-type':'application/json',
           'X-Api-Key':'abcd12345'}

for i in range(0,8):
    try:
        rr=requests.post(API_URL, data=json.dumps(message),headers=headers)
        rr
        print(rr)
        print("ok")
    except:
        print("error")
