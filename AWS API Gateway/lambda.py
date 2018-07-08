import boto3

def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    response = client.put_item(TableName="Kron",Item=event)
    return response
