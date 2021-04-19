# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 12:27:55 2021

@author: victo
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso, LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import mean_squared_log_error
from sklearn.preprocessing import StandardScaler

# GET DUMMY DATA 
train = pd.read_csv('train_selected.csv')
test = pd.read_csv('test_selected.csv')

train = train[[ 'House_age', 'Remodeled', 'YearRemodAdd', 'YearBuilt',
       'TotRmsAbvGrd', 'FullBath', '1stFlrSF', 'TotalBsmtSF', 'GarageArea',
       'GarageCars', 'TotalSF', 'OverallQual', 'Neighborhood', 'BsmtQual',
       'HeatingQC', 'KitchenQual', 'GarageFinish', 'GarageType', 'SaleType',
       'SalePrice']]

test = test[[ 'House_age', 'Remodeled', 'YearRemodAdd', 'YearBuilt',
       'TotRmsAbvGrd', 'FullBath', '1stFlrSF', 'TotalBsmtSF', 'GarageArea',
       'GarageCars', 'TotalSF', 'OverallQual', 'Neighborhood', 'BsmtQual',
       'HeatingQC', 'KitchenQual', 'GarageFinish', 'GarageType', 'SaleType',
       'SalePrice']]


train_dum = pd.get_dummies(train)
test_dum = pd.get_dummies(test)
test_dum.drop('SalePrice',inplace = True,axis=1)
test_dum = test_dum.dropna()
non = test_dum.isna().sum()

# sc = StandardScaler()
# train_dum = sc.fit_transform(train_dum)

missing = test.isna().sum().reset_index()
missing = missing[missing[0] > 1] 

y = train_dum['SalePrice'].values
train_dum.drop('SalePrice', inplace = True, axis=1)
X = train_dum.to_numpy(float)


#MUKTIPLE LINEAR REGRESSION

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
scaler = StandardScaler()

regr  = LinearRegression().fit(X_train, y_train)
regr.score(X_train, y_train)
regr.coef_
y_pred = regr.predict(X_test)
regr.score(X_train, y_train)

MSLE= mean_squared_log_error(y_test,y_pred)
print(f'OLS MSLE = {MSLE}')
MSE=mean_squared_error(y_test,y_pred)
print(f'OLS MSE = {MSE}')


### Ridge regression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

clf = Ridge(alpha=0.0001)
clf.fit(X_train, y_train)
clf.score(X_train, y_train)

#Lasso
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

clf = Lasso(alpha=0.1)
clf.fit(X_train, y_train)
clf.score(X_train, y_train)





c1 = train_dum.columns
c2 = test_dum.columns

for i in range(0, len(c2)):
    if (c2[i] in c1) == False:
        print(c2[i])
        
test_dum.drop('KitchenQual_None',inplace = True,axis=1)
test_predict = regr.predict(test_dum)

a = np.arange(1461,2920)
b= a.reshape(-1,1)
d={'Id': a, 'SalePrice':test_predict}
final = pd.DataFrame(data=d)

final.to_csv('Sub_1.csv', index=False)












































