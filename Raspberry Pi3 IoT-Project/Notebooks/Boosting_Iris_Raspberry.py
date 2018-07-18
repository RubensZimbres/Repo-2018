import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn import datasets
from sklearn.utils import shuffle

iris = datasets.load_iris()

learning_rate = 0.015
decay_rate = 5e-6
momentum = 0.9
epochs=50

scaler = MinMaxScaler(feature_range=(0, 1))

X_train2=scaler.fit_transform(iris.data[:,0:4])
Y_train = np.array(iris.target).reshape((150,1))

data=np.concatenate([X_train2,Y_train],axis=1)
data2=shuffle(data)

x_train=np.array(data2.T[0:4]).T
y_train=np.array(data2.T[4])

model=GradientBoostingClassifier(
init= None,
learning_rate= 0.1,
loss='deviance',
max_depth= 50,
max_features=2,
max_leaf_nodes=100,
min_samples_leaf= 1,
min_samples_split= 2,
min_weight_fraction_leaf= .2,
n_estimators= 100,
presort= 'auto',
random_state= None,
subsample= 1.0,
verbose=1,
warm_start= False)
model.fit(x_train,y_train)

res22=model.predict([x_train[0]])

import RPi.GPIO as GPIO 
from time import sleep 

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW) 

if res22[0]==0:
    GPIO.output(3, GPIO.HIGH)
elif res22[0]==1:
    GPIO.output(5, GPIO.HIGH)
else:
    GPIO.output(7, GPIO.HIGH)
    

