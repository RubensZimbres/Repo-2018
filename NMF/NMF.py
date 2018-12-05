import pandas as pd
import numpy as np
from sklearn.decomposition import NMF

V = np.array([[0,2,0,1,2,3,3],
              [2,3,1,1,3,2,4],
              [1,3,2,0,2,1,2],
              [0,4,0,4,1,1,0],
              [0,0,0,0,3,0,0]])

V = pd.DataFrame(V, columns=['User1', 'User2', 'User3', 'User4', 'User5', 'User6','User7'])
V.index = ['Soda', 'Bread', 'Fish', 'Meat', 'Coffee']
V

nmf = NMF(3)
nmf.fit(V)

H = pd.DataFrame(np.round(nmf.components_,2), columns=V.columns)
H.index = ['Class1', 'Class2',  'Class3']
H

W = pd.DataFrame(np.round(nmf.transform(V),2), columns=H.index)
W.index = V.index
W

reconstructed = pd.DataFrame(np.round(np.dot(W,H),2), columns=V.columns)
reconstructed.index = V.index
reconstructed
