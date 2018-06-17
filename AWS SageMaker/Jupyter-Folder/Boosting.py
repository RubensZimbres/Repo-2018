import pandas as pd
import numpy as np
import sagemaker
from sagemaker.predictor import csv_serializer
import boto3
import re
import os
from sagemaker import get_execution_role

role = get_execution_role()

df=pd.read_csv('s3://your-repo/DadosTeseLogit.csv',sep=',',header=0)
sel=np.where(df.corr()['selected']>.5)[0][0:-1]
df=df.iloc[:,np.concatenate([[30],sel])]

containers  = {'us-east-1': 'aws_account_id.dkr.ecr.us-east-1.amazonaws.com/decision-trees:latest'}

bucket =  'your-repo'
prefix = 'sagemaker/xgboost-churn'

df.to_csv('train.csv',header=False, index=False)
boto3.Session().resource('s3').Bucket(bucket).Object(os.path.join(prefix, 'train/train.csv')).upload_file('train.csv')
s3_input_train = sagemaker.s3_input(s3_data='s3://{}/{}/train'.format(bucket, prefix), content_type='csv')

containers[boto3.Session().region_name]

sess  =  sagemaker.Session()

xgb = sagemaker.estimator.Estimator(containers[boto3.Session().region_name],
                                    role, 
                                    train_instance_count=1, 
                                    train_instance_type='ml.m4.xlarge',
                                    output_path='s3://{}/{}/output'.format(bucket, prefix),
                                    sagemaker_session=sess)
                                    
xgb.fit({'train': s3_input_train})

xgb_predictor = xgb.deploy(initial_instance_count=1,instance_type='ml.m4.xlarge')

xgb_predictor.content_type = 'text/csv'
xgb_predictor.serializer = csv_serializer
xgb_predictor.deserializer = None

df3=df.iloc[:,[1,2,3]]
predictions =xgb_predictor.predict(df3.values).decode('utf-8')
predictions
