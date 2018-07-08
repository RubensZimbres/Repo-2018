import requests
import json
API_URL = "https://abcd12345.execute-api.us-east-1.amazonaws.com/stage"

mess ={"TableName":"Kron","Item":{"type":{"S":"22"},"page":{"S":"2"}}}

headers = {'Content-Type':'application/json',
           'Authorization':'abcd12345'}
loopCount =0
for i in range(0,8):
    try:
        message = {}
        message['message'] = mess
        message['sequence'] = loopCount
        messageJson = json.dumps(message)
        rr=requests.post(API_URL, data=messageJson,headers=headers)
        rr
        print(rr)
        print("ok")
        loopCount += 1
    except:
        print("error")
