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
! docker tag hello-world aws_account_id.dkr.ecr.us-east-1.amazonaws.com/sklearn
! aws ecr get-login --no-include-email
! docker push aws_account_id.dkr.ecr.us-east-1.amazonaws.com/sklearn
```  

Be sure to set up your SageMaker permissions on AWS.  
