# AWS API Gateway to collect and store sensor data

<b>Steps:</b>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/overview.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/POST.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/POST_Method_Request.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/POST_Integration_Request1.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/POST_Integration_Request2.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/POST_Integration_Response.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/POST_Method_Response.png>  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/Model_Schema.png>  

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
```
{
	"$schema": "http://json-schema.org/draft-04/schema#",
	"title": "Kron",
	"type": "object",
	"properties": {
		"TableName": {
			"type": "string"
		},
		"Item": {
			"type": "array",
			"items": {
				"type": "object",
				"properties": {
					"type": {
						"type": "string"
					},
					"page": {
						"type": "string"
					}
				}
			}
		}
	}
}
```  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20API%20Gateway/Pictures/API_Gateway_Success.png>  

