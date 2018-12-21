from sklearn.ensemble import RandomForestClassifier

from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score,precision_score,confusion_matrix,f1_score,recall_score

def accuracy(params):
    clf = RandomForestClassifier(**params)
    clf.fit(x_train,y_train)
    return clf.score(x_test, y_test)


parameters = {
    'max_depth': hp.choice('max_depth', range(80,120)),
    'max_features': hp.choice('max_features', range(30,x_train.shape[1])),
    'n_estimators': hp.choice('n_estimators', range(30,100)),
    "max_leaf_nodes":hp.choice("max_leaf_nodes",range(2,8)),
    "min_samples_leaf":hp.choice("min_samples_leaf",range(1,30)),
    "min_samples_split":hp.choice("min_samples_split",range(2,100)),
    'criterion': hp.choice('criterion', ["gini", "entropy"])}


best = 0
def f(params):
    global best
    acc = accuracy(params)
    if acc > best:
        best = acc
    print ('Improving:', best, params)
    return {'loss': -acc, 'status': STATUS_OK}

trials = Trials()

best = fmin(f, parameters, algo=tpe.suggest, max_evals=100, trials=trials)
print ('best:',best)
