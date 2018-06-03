# AWS SageMaker - Create you own Docker Image and Customized Algorithm

<b>Guidelines:</b>  

Open Jupyter Notebook and ssh into your SageMaker EC2 instance:

```
! sudo yum update -y
! sudo yum install -y docker
!sudo service docker start
!sudo usermod -a -G docker ec2-user
!docker info
!docker build Docker_Image.txt
```  

This process will take 2 hours in a ml.t2.medium SageMaker instance.  


