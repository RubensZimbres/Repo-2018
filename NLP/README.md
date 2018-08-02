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
```  
Use FastText_Português.py  

<b> 2. Gensim Word2Vec </b>  

Download trained model wiki.pt-br.word2vec.model at Repo-2017 Data folder.  

Use NLP_Word2Vec_Português.py
