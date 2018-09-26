import xgboost as xgb
y_test=np.array(YY[0:start].reshape(1,-1)[0])
x_test=np.array(XX.iloc[0:start,selected])
dtrain = xgb.DMatrix(x2, label=y2)
dtest=xgb.DMatrix(x_test, label=y_test)
param = {'max_depth': 20, 'eta': 1, 'silent': 1, 'objective': 'binary:logistic'}
evallist = [(dtrain, 'train')]
num_round = 10

feature_names=dict(np.array([range(0,XX.shape[1]),np.array(XX.columns)]).T)

bst = xgb.train(param, dtrain, num_round, evallist)
#bst.save_model('0001.model')
#bst.dump_model('dump.raw.txt')

pred01 = bst.predict(dtrain)
Y=y2

pred=[]
for cutoff in np.linspace(0.001,0.999,2000):
    pred0[pred0<cutoff]=0
    pred0[pred0!=0]=1
    pred.append(accuracy_score(np.array(Y),pred0))

thre=np.linspace(0.001,0.999,2000)[np.where(pred==np.max(pred))[0][0]]

pred01[pred01>=thre]=1
pred01[pred01<thre]=0

print 'Accuracy Score:',accuracy_score(np.array(Y),pred01)
print 'Precision (FP):',precision_score(np.array(Y),pred01,average='binary')
print 'Recall (FN):',recall_score(np.array(Y),pred01,average='binary')
print 'f1:',f1_score(np.array(Y),pred01,average='binary')
print confusion_matrix(np.array(Y),pred01),'\n'


pred011 = bst.predict(dtest)
Y=YY[0:start]

pred=[]
for cutoff in np.linspace(0.001,0.999,2000):
    pred0[pred0<cutoff]=0
    pred0[pred0!=0]=1
    pred.append(accuracy_score(np.array(Y),pred0))

thre=np.linspace(0.001,0.999,2000)[np.where(pred==np.max(pred))[0][0]]

pred011[pred011>=thre]=1
pred011[pred011<thre]=0


print 'Accuracy Score:',accuracy_score(np.array(Y),pred011)
print 'Precision (FP):',precision_score(np.array(Y),pred011,average='binary')
print 'Recall (FN):',recall_score(np.array(Y),pred011,average='binary')
print 'f1:',f1_score(np.array(Y),pred011,average='binary')
print confusion_matrix(np.array(Y),pred011),'\n'

