# AWS SageMaker - Create your own Docker Image and run Customized Algorithms (ongoing project)

<b>Guidelines:</b>  

Be sure to set up your SageMaker Execution Role Policy permissions on AWS IAM (besides S3):  

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ecr:*"            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ecs:*"            ],
            "Resource": "*"
        }

    ]
}
```

Start instance in SageMaker and Open notebook.  

Select Python 2 environment  

Open Jupyter Notebook from your SageMaker instance and run:

```
! sudo yum update -y
! sudo yum install -y docker
! sudo service docker start
! sudo usermod -a -G docker ec2-user
! docker info
! docker build -t decision-trees .
! aws ecr create-repository --repository-name decision-trees
! docker tag decision-trees aws_account_id.dkr.ecr.us-east-1.amazonaws.com/decision-trees
! aws ecr get-login --no-include-email
! docker login -u abc -p abc12345 http://abc123
! docker push aws_account_id.dkr.ecr.us-east-1.amazonaws.com/decision-trees
! docker images
! aws ecs register-task-definition --cli-input-json file://decision-trees-task-def.json
#! aws ecs run-task --task-definition decision-trees
```  

Copy files necessary to run your Machine Learning model:  

```
docker cp train sklearn:/opt/ml/model/train
```  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20SageMaker/pics/Docker_structure.png>     
  

<b>WARNING: </b> If you are making experiments with SageMaker or even learning how to use it, be aware that <b>each model</b> (with a ml.t2.medium instance) with its corresponding endpoint and trained on a ml.m4.4xlarge instance will cost you an average of 6.00 USD a day. So, never leave 2 or 3 models running overnight otherwise your AWS bill will skyrocket.
