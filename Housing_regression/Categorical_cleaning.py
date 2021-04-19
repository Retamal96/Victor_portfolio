# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 20:23:33 2021

@author: victo
"""

# example of chi squared feature selection for categorical data
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from matplotlib import pyplot
quanti = []
quali = []
def nopo(row):
    if row['HeatingQC']=='Po':
        return None
    else:
        return row['HeatingQC']

def load_dataset_quali(filename):
    data = pd.read_csv(filename)
    train_data = data.iloc[0:1460]
    column = data.columns
    for col in column:
        if (data[col].dtype == 'int64') or  (data[col].dtype == 'float64'):
            quanti.append(col)
        else:
            quali.append(col)
    qualitative = train_data[quali]
    qualitative['HeatingQC']= qualitative.apply(lambda x: nopo(x), axis=1)
    dataset= qualitative.values
    X = dataset[:, :-1]
    y = dataset[:,-1]
    # y = y.reshape(-1,1)
    X = X.astype(str)
    return X, y

X,y = load_dataset_quali('data_clean.csv')


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1)

print('Train', X_train.shape, y_train.shape)
print('Test', X_test.shape, y_test.shape)

# prepare input data
def prepare_inputs(X_train, X_test):
	oe = OrdinalEncoder(handle_unknown = "ignore")
	oe.fit(X_train)
	X_train_enc = oe.transform(X_train)
	X_test_enc = oe.transform(X_test)
	return X_train_enc, X_test_enc

# prepare target
def prepare_targets(y_train, y_test):
	le = LabelEncoder()
	le.fit(y_train)
	y_train_enc = le.transform(y_train)
	y_test_enc = le.transform(y_test)
	return y_train_enc, y_test_enc

# feature selection
def select_features(X_train, y_train, X_test):
	fs = SelectKBest(score_func=chi2, k=12)
	fs.fit(X_train, y_train)
	X_train_fs = fs.transform(X_train)
	X_test_fs = fs.transform(X_test)
	return X_train_fs, X_test_fs, fs

# prepare input data
X_train_enc, X_test_enc = prepare_inputs(X_train, X_test)
# prepare output data
y_train_enc, y_test_enc = prepare_targets(y_train, y_test)
# feature selection
X_train_fs, X_test_fs, fs = select_features(X_train_enc, y_train_enc, X_test_enc)
# what are scores for the features
for i in range(len(fs.scores_)):
	print('Feature %d: %f' % (i, fs.scores_[i]))
# plot the scores
pyplot.bar([i for i in range(len(fs.scores_))], fs.scores_)
pyplot.show()


