import boto3

if __name__ == "__main__":
    fileName='street.jpg'
    bucket='bucket-xxx'
    
    client=boto3.client('rekognition',region_name='us-east-1')

    response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':fileName}})

    print('Detected labels for ' + fileName)    
    for label in response['Labels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))
