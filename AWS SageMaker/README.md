# AWS SageMaker - Create you own Docker Image and Customized Algorithm

<b>Guidelines:</b>  

Open Jupyter Notebook from your SageMaker instance and run:

```
! sudo yum update -y
! sudo yum install -y docker
! sudo service docker start
! sudo usermod -a -G docker ec2-user
! docker info
! docker build Docker_Image.txt
```  

This last line of code will take 2 hours to complete in a ml.t2.medium SageMaker instance.  


