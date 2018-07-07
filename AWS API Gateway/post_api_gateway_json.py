import requests

KERAS_REST_API_URL = "https://abcd12345.execute-api.us-east-1.amazonaws.com/stage"

payload ={"TableName":"Kron","Item":{"type":"22","page":"2"}}

headers = {'Content-Type':'application/json',
           'Authorization':'Abcd12345'}

for i in range(0,3):
    try:
        rr=requests.post(KERAS_REST_API_URL, data=payload,headers=headers)
        rr
        print(rr)
        print("ok")
    except:
        print("error")
