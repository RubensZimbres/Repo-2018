# Real-Time Streaming Data - Kibana  
  
<b>Install JAVA:</b>  

```
sudo apt-get install default-jre  
sudo apt-get install default-jdk

```  
If necessary, run:  
```
gksudo gedit /etc/environment
```  
Add PATH to environment variable

<b><Install Kibana:</b>  

```
wget https://artifacts.elastic.co/downloads/kibana/kibana-6.2.4-linux-x86_64.tar.gz
shasum -a 512 kibana-6.2.4-linux-x86_64.tar.gz 
tar -xzf kibana-6.2.4-linux-x86_64.tar.gz
cd kibana-6.2.4-linux-x86_64
```

<b><Install elasticsearch:</b>  
```
wget httpswget https://://artifactsartifacts..elasticelastic..coco//downloadsdownloads//elasticsearchelasticsearch//elasticsearchelasticsearch--6.26.2..4.zip4.zip
wget https wget https://://artifactsartifacts..elasticelastic..coco//downloadsdownloads//elasticsearchelasticsearch//elasticsearchelasticsearch--6.26.2..4.zip4.zip..sha512
shasum sha512 shasum --a a 512512  --c elasticsearchc elasticsearch--6.26.2..4.zip4.zip..sha512 sha512 
unzip elasticsearch unzip elasticsearch--6.26.2..4.zip4.zip
cd elasticsearch cd elasticsearch--6.26.2..44
```

<b><Install x-pack in Kibana:</b>  
```
bin/kibana-plugin install x-pack
```

<b><Install x-pack in elasticsearch:</b>  

```
bin/elasticsearch-plugin install x-pack
```


