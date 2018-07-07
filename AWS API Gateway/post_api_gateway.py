import requests

REST_API_URL = "https://abcd12345.execute-api.us-east-1.amazonaws.com/stage"

payload ={"type":'22',"page":'1'}
      
headers = {'Content-Type': 'application/json',
           'Authorization': 'acbd12345'}

for i in range(0,6):
    try:
        rr=requests.post(REST_API_URL, data=payload,headers=headers)
        rr
        print(rr)
        print("ok")
    except:
        print("error")
