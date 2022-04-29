import matplotlib.pyplot as plt;

import seaborn as sns;

import pandas as pd;

import numpy as np;

import sklearn as sk;

from sklearn.model_selection import train_test_split;

from sklearn.neighbors import KNeighborsClassifier;

from sklearn.metrics import confusion_matrix;

from sklearn.metrics import classification_report;

from sklearn.svm import SVC;

adult_columns="age workclass fnlwgt education education-num marital-status occupation relationship race sex capital-gain capital-loss hours-per-week native-country".split();

adults=pd.read_csv(r"C:\Users\benwo\Downloads\adult.data.csv",delimiter=",",na_values="?",names=adult_columns,index_col=False);

print(adults);






