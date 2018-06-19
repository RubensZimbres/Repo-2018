# AWS SageMaker - Create your own Docker Image and run Customized Algorithms

<b>Guidelines:</b>  

Be sure to set up your SageMaker Execution Role Policy permissions on AWS IAM (besides S3) and also AmazonEC2ContainerServiceFullAccess, AmazonEC2ContainerRegistryFullAccess and AmazonSageMakerFullAccess.  

Create and start instance in SageMaker and Open notebook.  

Clone this repo to your EC2 instance in SageMaker.

Inside Jupyter, run:

```
! sudo service docker start
! sudo usermod -a -G docker ec2-user
! docker info
! chmod +x decision_trees/train
! chmod +x decision_trees/serve
! aws ecr create-repository --repository-name decision-trees
! aws ecr get-login --no-include-email
! docker login -u abc -p abc12345 http://abc123
! docker build -t decision-trees .
! docker tag decision-trees aws_account_id.dkr.ecr.us-east-1.amazonaws.com/decision-trees:latest
! docker push aws_account_id.dkr.ecr.us-east-1.amazonaws.com/decision-trees:latest
! aws ecs register-task-definition --cli-input-json file://decision-trees-task-def.json
```  

Open and run Boosting.ipynb  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20SageMaker/pics/Sage_Maker_YES.png>

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20SageMaker/pics/Docker_structure.png>     
  
<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20SageMaker/pics/altert2.png>  
<b>WARNING: </b> If you are making experiments with SageMaker or even learning how to use it, be aware that <b>each model</b> (with a ml.t2.medium instance) with its corresponding endpoint and trained on a ml.m4.4xlarge instance will cost you an average of 5.00 USD a day. So, never leave 2 or 3 models running overnight otherwise your AWS bill will skyrocket. Also, take care of repositories created and tasks related to them, as well as any CloudWatch report.
