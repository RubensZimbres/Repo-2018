# Python Codes: IoT, Machine Learning, Computer Vision

Codes in Machine Learning, Deep Learning, Reinforcement Learning, Artificial Intelligence and Computer Vision

<b> Welcome to my GitHub repo. </b>

I am a Data Scientist and I code in Python. Here you will find some Machine Learning, Deep Learning, Natural Language Processing, Artificial Intelligence and Computer Vision models I developed.

Data for models available at:

https://drive.google.com/drive/folders/0B0RLknmL54khU2UwX3dnX1E1WHc?usp=sharing  
 
Keras version used in models: keras==2.0.8
Tensorflow version used in models: tensorflow==1.7.0  

<b> AWS API Gateway </b>  

This folder presents general guidelines to create an endpoint and API key in AWS API Gateway, that will receive data from a Python notebook sending sensor data, that arrives in API Gateway, is processed and cleaned in Lambda and is stored in DynamoDB. Data is then available for S3 to create a data pipeline and further visualization with Kibana or Quick Sight.

<b> AWS SageMaker </b>  

This sector presents the development of a Docker container with a customized Machine Learning model that is pushed into Elastic Container Registry and generates and endpoint in AWS SageMaker.

<b> COCO Model </b>

COCO (Common Objects in Context) is an image segmentation model. This folder presents my Pull Request regarding pycocotools library incompatibility between Python 2 and 3 suggesting a fix.  

<b> CPU Temperature - IoT Project at AWS</b>  

In this project I turned my notebook into an IoT device, where CPU temperature is collected via Linux command line run inside a Python notebook and then sent via MQTT protocol to Amazon AWS IoT service, integrated with DynamoDB, Data Pipeline, S3, Quick Sight and Cloud Watch. An alternative solution for near real-time data is also presented, using Kinesis, Firehose, Elasticsearch and Kibana.  

<b> CycleGAN Project </b> -  GANs <br/>

In this folder I presente the steps to train a CycleGAN for Style Transfer applied to paintings of Vincent van Gogh and Pablo Picasso using an EC2 GPU Tesla K-80. Examples of outputs are presented.  

<b> DEEP LEARNING SUMMER SCHOOL </b> -  GANs <br/>

In this folder you will find Tensorflow and Keras codes and also a Powerpoint presentation about GANs I developed for my lecture and workshop at the first Deep Learning Summer School in Brazil, at Goiás.  

<b> EC2 INSTANCE SETUP </b>

A set up Manual I developed to create EC2 instances in Amazon AWS  

<b> FLASK </b>  

This folder contains the Python code for the REST API and also the request code.

<b> KERAS </b>
 
GANs: Generative Adversarial Networks
 
DCGANs: Deep Convolutional Generative Adversarial Networks  
 
<b> NLP </b>  

Notebooks presenting Word2Vec similarities in trained Wikipedia corpus, Portuguese language.  

<b> OPENCV </b>
 
In this folder you will find a guide to create your own haarcascade.xml so that you can identify any object using OpenCV.  
 
<b> Raspberry Pi3 - IoT Project</b>  

In this project I use Raspberry Pi3 running in Ubuntu Core OS and attached a sensor and then send telemetry data to Amazon AWS IoT service, integrated with DynamoDB, S3, Quick Sight and Cloud Watch. I also plan to deploy a Deep Learning trained model into the device for classification purposes.  

<img src=https://github.com/RubensZimbres/Repo-2018/raw/master/Raspberry%20Pi3%20IoT-Project/Pictures/small_kit.png>

<b> TENSORFLOW </b> 
 
Model for Regression
 
Model for Classification 
 
LSTM: Long Short Term Memory Neural Networks
 
GANs: Generative Adversarial Networks
 
DCGANs: Deep Convolutional Generative Adversarial Networks
 
InfoGANs </b> Mutual Information Adversarial Networks where loss function is customized. 
Mutual Info = H(B)-Sum(P(B=b).H(A|B=b)

Tensorboard: visualization of Tensorflow models' training  
 
 
<b> SEG-NET </b> : Image Segmentation with SEG-NET  
 
<b> SMOTE </b> : Synthetic Minority Oversampling Technique for imbalanced classes  

<b> YOLO Model </b>

The YOLO Model (You Only Look Once) is a Deep Learning project for Real-Time object detection. Examples of outputs are presented.

Datasets available at Repo-2017  

<img src=https://github.com/RubensZimbres/Repo-2018/raw/master/COCO%20model/Pictures/COCO_result_BIG.png>
 
<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Deep%20Learning%20Summer%20School/GANs.jpg>
 
 
<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Deep%20Learning%20Summer%20School/GAN_Best.PNG>

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Deep%20Learning%20Summer%20School/TensorBoard_Loss.PNG>

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/Deep%20Learning%20Summer%20School/TensorBoard_Structure.PNG>

<img src=https://github.com/RubensZimbres/Repo-2018/raw/master/YOLO%20model/YOLO.png>

<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/OpenCV/Training_Haar.png>

