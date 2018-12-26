from xgboost import XGBClassifier

from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score,precision_score,confusion_matrix,f1_score,recall_score

def accuracy(params):
    clf = XGBClassifier(**params,learning_rate=0.7, n_estimators=6, objective='binary:logistic', 
                    booster='gbtree', n_jobs=64,eval_metric="error",eval_set=eval_set, verbose=True)
    clf.fit(x_train,y_train,eval_set=eval_set, verbose=True)
    return clf.score(x_test, y_test)

eval_set=eval_set = [(x_test, y_test)]


parameters = {
    'max_depth': hp.choice('max_depth', range(80,120)),
    'gamma': hp.choice('gamma', range(0,10)),
    "min_child_weight":hp.choice("min_child_weight",range(0,1)),
    "max_delta_step":hp.choice("max_delta_step",range(0,10))}


best = 0
def f(params):
    global best
    acc = accuracy(params)
    if acc > best:
        best = acc
    print ('Improving:', best, params)
    return {'loss': -acc, 'status': STATUS_OK}

trials = Trials()

best = fmin(f, parameters, algo=tpe.suggest, max_evals=50, trials=trials)
print ('best:',best)
