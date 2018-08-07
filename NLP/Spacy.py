documents = ["Interface máquina humana para aplicações computacionais de laboratório abc",
              "Um levantamento da opinião do usuário sobre o tempo de resposta do sistema informático",
               "O sistema de gerenciamento de interface do usuário EPS",
               "Sistema e testes de engenharia de sistemas humanos de EPS",
               "Relação do tempo de resposta percebido pelo usuário para a medição de erro",
               "A geração de árvores não ordenadas binárias aleatórias",
               "O gráfico de interseção dos caminhos nas árvores personalizadas",
               "Gráfico de menores IV Largura de árvores personalizadas e bem quase encomendado",
               "Gráficos menores Uma pesquisa"]

# from nltk.stem import WordNetLemmatizer
# lemmatizer = WordNetLemmatizer()

import spacy
from spacy.lang.pt.examples import sentences

!python -m spacy download pt_core_news_sm

nlp = spacy.load('pt_core_news_sm')

long_words1=[[nlp(str(i)) for i in documents[k].lower().split() if len(i)>3] for k in range(0,9)] 

