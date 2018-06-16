# AWS SageMaker - Create your own Docker Image and run Customized Algorithms

<b>Guidelines:</b>  

Be sure to set up your SageMaker Execution Role Policy permissions on AWS IAM (besides S3): AmazonEC2ContainerServiceFullAccess, AmazonEC2ContainerRegistryFullAccess and AmazonSageMakerFullAccess.   

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

In the same Jupyter notebook, you may run:  

```
#! docker run -i -t 1234567.dkr.ecr.us-east-1.amazonaws.com/decision-trees
```  

Open new notebook in Jupyter. Run:  
```
! docker ps
CONTAINER ID        IMAGE                                                         COMMAND             CREATED             STATUS              PORTS               NAMES
123456abc        1234567.dkr.ecr.us-east-1.amazonaws.com/decision-trees   "/bin/bash"         21 seconds ago      Up 20 seconds                           dreamy_lichterman
! docker images
```  
Run Boosting.ipynb  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20SageMaker/pics/Sage_Maker_YES.png>

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20SageMaker/pics/Docker_structure.png>     
  
<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20SageMaker/pics/altert2.png>  
<b>WARNING: </b> If you are making experiments with SageMaker or even learning how to use it, be aware that <b>each model</b> (with a ml.t2.medium instance) with its corresponding endpoint and trained on a ml.m4.4xlarge instance will cost you an average of 5.00 USD a day. So, never leave 2 or 3 models running overnight otherwise your AWS bill will skyrocket. Also, take care of repositories created and tasks related to them, as well as any CloudWatch report.
