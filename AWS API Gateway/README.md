# AWS API Gateway to collect and store sensor data in DynamoDB Table via Lambda Function

<b>Steps:</b>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/overview.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/POST.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/POST_Method_Request.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/POST_Integration_Request1.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/POST_Integration_Request2.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/POST_Integration_Response.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/POST_Method_Response.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/cors.png>

Model schemas:  
  
https://www.liquid-technologies.com/online-json-to-schema-converter

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "MessageID": {
      "type": "object",
      "properties": {
        "S": {
          "type": "string"
        }
      },
      "required": [
        "S"
      ]
    },
    "type": {
      "type": "object",
      "properties": {
        "S": {
          "type": "string"
        }
      },
      "required": [
        "S"
      ]
    },
    "page": {
      "type": "object",
      "properties": {
        "S": {
          "type": "string"
        }
      },
      "required": [
        "S"
      ]
    }
  },
  "required": [
    "MessageID",
    "type",
    "page"
  ]
}
```  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/API_Gateway_Success.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/lambda_1.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/dynamo_API.png>  
