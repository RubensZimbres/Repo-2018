# AWS API Gateway to collect and store sensor data in DynamoDB Table

<b>Steps:</b>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/overview.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/POST.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/POST_Method_Request.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/POST_Integration_Request1.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/POST_Integration_Request2.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/POST_Integration_Response.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/POST_Method_Response.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/Model_Schema.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/cors.png>

Model schemas:  

```
{
  "type" : "object",
  "properties" : {
    "type" : {
      "type" : "string"
    },
    "page" : {
      "type" : "number"
    }
  }
}
```  
https://www.liquid-technologies.com/online-json-to-schema-converter

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "TableName": {
      "type": "string"
    },
    "Item": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string"
        },
        "page": {
          "type": "string"
        }
      },
      "required": [
        "type",
        "page"
      ]
    }
  },
  "required": [
    "TableName",
    "Item"
  ]
}```  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/API_Gateway_Success.png>  

