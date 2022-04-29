"""

Classification

"""
import matplotlib.pyplot as plt;

import seaborn as sns;

import pandas as pd;

import numpy as np;

import sklearn as sk;

from sklearn.model_selection import train_test_split;

from sklearn.neighbors import KNeighborsClassifier;

from sklearn.metrics import confusion_matrix;

from sklearn.metrics import classification_report;

iris=pd.DataFrame(sns.load_dataset("iris"));


y= iris.pop("species");
X=iris;

Xtrain,Xtest,ytrain,ytest=train_test_split(X,y,test_size=0.5,stratify=y);

model = KNeighborsClassifier();

model.fit(Xtrain,ytrain);

ypredict = model.predict(Xtest);

accuracy= (ypredict ==ytest).sum() / len(ytest) *100;

model.score(Xtest,ytest);

"""

Precision= true positives/(true positives+false positives)

Recall= Trye positives/ (true positives + false negatives)

F1 Score= 2*((Precision+Recall)/(Precision+Recall)) ?

"""

labels="versicolor virginica".split();

cmat=confusion_matrix(ytest,ypredict,labels=labels);

sns.heatmap(cmat,cmap=plt.cm.Blues, xticklabels=labels,yticklabels=labels);

clf_rpt=classification_report(ytest,ypredict,labels=labels);

print(clf_rpt);

mpg= sns.load_dataset("mpg");





