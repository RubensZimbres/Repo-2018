import boto3

def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    response = client.put_item(TableName="Table2",Item=event)
    return response
