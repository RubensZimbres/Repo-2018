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
Create a Cluster in Elastic Container Service.  

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
```  

Associate the task created with the cluster. Set up permissions in your ECS repository. In the same Jupyter notebook, run:  

```
! docker run -i -t 1234567.dkr.ecr.us-east-1.amazonaws.com/decision-trees
```  

Docker is running and you can add files to image. Open new notebook in Jupyter. Run:  
```
! docker ps
CONTAINER ID        IMAGE                                                         COMMAND             CREATED             STATUS              PORTS               NAMES
123456abc        1234567.dkr.ecr.us-east-1.amazonaws.com/decision-trees   "/bin/bash"         21 seconds ago      Up 20 seconds                           dreamy_lichterman
```

#Copy files necessary to run your Machine Learning model:  

```
! docker cp decision_trees/nginx.conf 123456abc:nginx.conf
! docker cp decision_trees/predictor.py 123456abc:predictor.py
! docker cp decision_trees/serve 123456abc:serve
! docker cp decision_trees/train 123456abc:train
! docker cp decision_trees/wsgi.py 123456abc:wsgi.py
```  

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20SageMaker/pics/Docker_structure.png>     
  
<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/AWS%20SageMaker/pics/altert2.png>  
<b>WARNING: </b> If you are making experiments with SageMaker or even learning how to use it, be aware that <b>each model</b> (with a ml.t2.medium instance) with its corresponding endpoint and trained on a ml.m4.4xlarge instance will cost you an average of 6.00 USD a day. So, never leave 2 or 3 models running overnight otherwise your AWS bill will skyrocket.
