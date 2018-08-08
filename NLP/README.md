# Natural Language Processing - Wikipedia Word Embeddings in Portuguese  

<b> 1. Facebook Fast Text </b>  

Install FastText, chakin and download trained model:  

```
git clone https://github.com/facebookresearch/fastText.git
cd fastText
pip install .

pip install chakin
import chakin
chakin.search(lang='Portuguese')

           Name  Dimension     Corpus VocabularySize    Method    Language     Author  
8  fastText(pt)        300  Wikipedia           592K  fastText  Portuguese   Facebook 

chakin.download(number=8, save_dir='./')

(OR)

wget https://s3-us-west-1.amazonaws.com/fasttext-vectors/wiki.pt.vec (1.5 GB)
wget https://s3-us-west-1.amazonaws.com/fasttext-vectors/wiki.pt.zip (3.9 GB)

```  
Use Facebook_FastText_Português.py  

  

<b> 2. Word2Vec </b>  

Download trained model wiki.pt-br.word2vec.model at Repo-2017 Data folder.  

Use Word2Vec_Português.py

<b> 3. GloVe </b> 

```
wget http://143.107.183.175:22980/download.php?file=embeddings/glove/glove_s300.zip  (1.6 GB)  
```  

Use Glove_Wikipedia_PT.py
