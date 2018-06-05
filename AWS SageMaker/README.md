# AWS SageMaker - Create your own Docker Image and run Customized Algorithms

<b>Guidelines:</b>  

Open Jupyter Notebook from your SageMaker instance and run:

```
! sudo yum update -y
! sudo yum install -y docker
! sudo service docker start
! sudo usermod -a -G docker ec2-user
! docker info
! docker build -t sklearn .
! aws ecr create-repository --repository-name sklearn
! docker tag sklearn aws_account_id.dkr.ecr.us-east-1.amazonaws.com/sklearn
! aws ecr get-login --no-include-email
! docker login -u abc -p abc12345 http://abc123
! docker push aws_account_id.dkr.ecr.us-east-1.amazonaws.com/sklearn
! docker images
! aws ecs register-task-definition --cli-input-json file://sklearn-task-def.json
! aws ecs run-task --task-definition sklearn
```  

Be sure to set up your SageMaker Execution Role Policy permissions on AWS (besides S3):  

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
<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20SageMaker/altert2.png><b>WARNING: </b> If you are making experiments with SageMaker or even learning how to use it, be aware that each model with its corresponding endpoint running on a ml.m4.4xlarge instance will cost you an average of 6.00 USD a day. So, never leave 2 or 3 models running overnight otherwise your AWS bill will skyrocket.
