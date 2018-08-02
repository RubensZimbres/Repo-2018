# Natual Language Processing - Wikipedia Word Embeddings in Portuguese  

<b>1. Fast Text </b>  

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
Use FastText.py
