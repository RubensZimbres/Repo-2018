from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
from sklearn.model_selection import cross_val_score

def accuracy(params):
    clf = RandomForestClassifier(**params)
    return cross_val_score(clf, x, y).mean()

parameters = {
    'max_depth': hp.choice('max_depth', range(30,60)),
    'max_features': hp.choice('max_features', range(3,4)),
    'n_estimators': hp.choice('n_estimators', range(100,150)),
    "max_leaf_nodes":hp.choice("max_leaf_nodes",range(3,10)),
    "min_samples_leaf":hp.choice("min_samples_leaf",range(1,40)),
    "min_samples_split":hp.choice("min_samples_split",range(2,40)),
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
