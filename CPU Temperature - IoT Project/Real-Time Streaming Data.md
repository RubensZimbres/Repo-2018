# Real-Time Streaming Data - AWS IoT + Kinesis + Lambda + Elasticsearch + Kibana  
  
<b>Start sending data to AWS IoT Core via MQTT</b>  

<b>Create a Domain in Amazon Elasticsearch</b>  

<b>Create a Kinesis data stream</b>  

<b>Clean Data Being Sent with Lambda</b>

<b>Install JAVA locally:</b>  

```
sudo apt-get install default-jre  
sudo apt-get install default-jdk

```  
If necessary, run:  
```
gksudo gedit /etc/environment
```  
Add PATH to environment variable

<b>Install Kibana:</b>  

```
wget https://artifacts.elastic.co/downloads/kibana/kibana-6.2.4-linux-x86_64.tar.gz
shasum -a 512 kibana-6.2.4-linux-x86_64.tar.gz 
tar -xzf kibana-6.2.4-linux-x86_64.tar.gz
cd kibana-6.2.4-linux-x86_64
```

<b>Install elasticsearch:</b>  
```
wget httpswget https://://artifactsartifacts..elasticelastic..coco//downloadsdownloads//elasticsearchelasticsearch//elasticsearchelasticsearch--6.26.2..4.zip4.zip
wget https wget https://://artifactsartifacts..elasticelastic..coco//downloadsdownloads//elasticsearchelasticsearch//elasticsearchelasticsearch--6.26.2..4.zip4.zip..sha512
shasum sha512 shasum --a a 512512  --c elasticsearchc elasticsearch--6.26.2..4.zip4.zip..sha512 sha512 
unzip elasticsearch unzip elasticsearch--6.26.2..4.zip4.zip
cd elasticsearch cd elasticsearch--6.26.2..44
```

<b>Install x-pack in Kibana:</b>  
```
bin/kibana-plugin install x-pack
```

<b>Install x-pack in elasticsearch:</b>  

```
bin/elasticsearch-plugin install x-pack
```  

<b>Edit kibana.yml and elasticsearch.yml</b>  

Kibana:  
```
server.port:5601
server.host:"localhost"
elasticsearch.url: "https://search-domain-12345abcd.us-east-1.es.amazonaws.com:9200"
elasticsearch.password: "s0m3th1ngs3cr3t"
xpack.security.encryptionKey: "something_at_least_32_characters"
xpack.security.sessionTimeout: 600000
xpack.reporting.encryptionKey: "something_secret"
```  
elasticsearch:  `
```
cluster.name: 1234567890:domain  
```
<img src=https://github.com/RubensZimbres/Repo-2018/blob/master/CPU%20Temperature%20-%20IoT%20Project/Pictures/Alternative_Solution.png>  

