import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import matplotlib.pyplot as plt
from gensim import corpora
documents = ["Interface máquina humana para aplicações computacionais de laboratório abc",
              "Um levantamento da opinião do usuário sobre o tempo de resposta do sistema informático",
               "O sistema de gerenciamento de interface do usuário EPS",
               "Sistema e testes de engenharia de sistemas humanos de EPS",
               "Relação do tempo de resposta percebido pelo usuário para a medição de erro",
               "A geração de árvores não ordenadas binárias aleatórias",
               "O gráfico de interseção dos caminhos nas árvores personalizadas",
               "Gráfico de menores IV Largura de árvores personalizadas e bem quase encomendado",
               "Gráficos menores Uma pesquisa"]

# remove common words and tokenize
stoplist = set('a e o para sobre'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
    for document in documents]
texts=[[x.lower() for x in texts[i]] for i in range(0,9)]

long_words1 = [[w for w in texts[i] if len(w)>4] for i in range(0,9)]

import gensim
from gensim.corpora import  WikiCorpus
from gensim.models import Word2Vec
from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('/home/rubens/Downloads/glove_s300.txt')

model.most_similar(positive=['rainha', 'mulher'], negative=['homem'])

ff=[]
for i in range(0,len(documents)):
    ff.append([model.wv[x] for x in long_words1[i]])

from sklearn.metrics.pairwise import cosine_similarity

model.wv.most_similar(positive="personalizar")

frase="quero um teste de engenharia"
long_words=[w for w in frase.lower().split() if len(w)>3]  

r=[model.wv[x] for x in long_words]

## NEED TO LEMMATIZE

import numpy as np
print('\n',frase,'\n')
for i in range(0,9):
    print(i,np.sum(cosine_similarity(r,ff[i])),documents[i])

model.wv.most_similar(positive="personalizar")

[('configurar', 0.4632694721221924),
 ('personalização', 0.4522443413734436),
 ('visualizar', 0.43862223625183105),
 ('customizar', 0.4385221600532532),
 ('widgets', 0.43387433886528015),
 ('seleccionar', 0.42364561557769775),
 ('adicionar', 0.4226790964603424),
 ('personalizados', 0.42068400979042053),
 ('usuário', 0.4146319031715393),
 ('personalizadas', 0.4089478552341461)]
