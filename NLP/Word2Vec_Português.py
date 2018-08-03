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

stoplist = set('a e o para sobre'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
    for document in documents]
texts=[[x.lower() for x in texts[i]] for i in range(0,9)]

long_words1 = [[w for w in texts[i] if len(w)>4] for i in range(0,9)]

import gensim
from gensim.corpora import  WikiCorpus
from gensim.models import Word2Vec

outp = "/home/rubens/Documents/Python/Wikipedia/wiki.pt-br.word2vec.model"

model = gensim.models.Word2Vec.load(outp)

model.most_similar(positive=['rainha', 'mulher'], negative=['homem'])

ff=[]
for i in range(0,len(documents)):
    ff.append([model[x] for x in long_words1[i]])

from sklearn.metrics.pairwise import cosine_similarity

for i in range(0,9):
    print(i,documents[i])

### Sem preposição e artigo

frase="quero uma customização de árvores"
long_words = [w for w in frase.lower().split() if len(w)>3]


r=[model.wv[x] for x in long_words]

import numpy as np
print('\n',frase,'\n')
for i in range(0,9):
    print(i,np.sum(cosine_similarity(r,ff[i])),documents[i])
    
###################################################################

model.most_similar(positive='customizar')

[('personalizar', 0.8436061143875122),
 ('desbloquear', 0.697656512260437),
 ('destravar', 0.6670040488243103),
 ('emular', 0.6302285194396973),
 ('configurar', 0.6297141313552856),
 ('atualizar', 0.6150598526000977),
 ('acessar', 0.608622670173645),
 ('sincronizar', 0.6048502922058105),
 ('renderizar', 0.6007644534111023),
 ('programar', 0.5998499393463135)]

