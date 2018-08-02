from __future__ import print_function
from gensim.models import KeyedVectors

pt_model = KeyedVectors.load_word2vec_format('/home/rubens/Documents/Python/Wikipedia/chakin_FastText/wiki.pt.vec')

words = []
for word in pt_model.vocab:
    words.append(word)

print("# Tokens: {}".format(len(words)))

print("Vector dimension: {}".format(len(pt_model[words[0]])))
    
print("Word components example: {}".format(pt_model[words[0]]))

find_similar_to = 'carro'

for similar in pt_model.similar_by_word(find_similar_to):
    print("Word: {0}, Similarity: {1:.2f}".format(similar[0], similar[1]))
    
word_plus = ['homem', 'rei']
word_minus = ['poder']

# Necessary to clean the similarity result:

for similar in pt_model.most_similar(positive=word_plus, negative=word_minus):
    print("Word : {0} , Similarity: {1:.2f}".format(similar[0], similar[1]))
 
