# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 12:20:58 2021

@author: victo
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2


house_data= pd.read_csv('data_clean.csv')
house_data = house_data[['Id', 'MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea', 'Street',
       'Alley', 'LotShape', 'LandContour', 'Utilities', 'LotConfig',
       'LandSlope', 'Neighborhood', 'Condition1', 'Condition2', 'BldgType',
       'HouseStyle', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd',
       'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType',
       'MasVnrArea', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual',
       'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinSF1',
       'BsmtFinType2', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'Heating',
       'HeatingQC', 'CentralAir', 'Electrical', '1stFlrSF', '2ndFlrSF',
       'LowQualFinSF', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath',
       'BedroomAbvGr', 'KitchenAbvGr', 'KitchenQual', 'TotRmsAbvGrd',
       'Functional', 'Fireplaces', 'FireplaceQu', 'GarageType', 'GarageYrBlt',
       'GarageFinish', 'GarageCars', 'GarageArea', 'GarageQual', 'GarageCond',
       'PavedDrive', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch',
       'ScreenPorch', 'PoolArea', 'PoolQC', 'Fence', 'MiscFeature', 'MiscVal',
       'MoSold', 'YrSold', 'SaleType', 'SaleCondition', 'SalePrice',
       'House_age', 'Remodeled', 'TotalSF', 'TotalPorch',
       'number_of_exteriors']]
column = house_data.columns

quanti = []
quali = []

def add_quanti(column):
    for col in column:
        if (house_data[col].dtype == 'int64') or  (house_data[col].dtype == 'float64'):
            quanti.append(col)
        else:
            quali.append(col)

add_quanti(column)
quantitative = house_data[quanti]
qualitative = house_data[quali]

## FEATURE SELECTION AND CORRELATION 

#Quantitative selection  
corrs = house_data.corr()
corr_pairs = corrs.unstack()

sorted_pairs = corr_pairs.sort_values(kind="quicksort")

strong_pairs = sorted_pairs[abs(sorted_pairs) > 0.5]

final_quanti_a = list(strong_pairs.loc['SalePrice'].index)
final_quanti = final_quanti_a[0:12]

corrs2 = house_data[final_quanti].corr()

sns.heatmap(corrs2, annot = True,cmap="BuPu")
plt.show()

#Qualitative selection 

quanti = []
quali = []

def load_dataset_quali(Dataframe):
    data = Dataframe
    train_data = data.iloc[0:1460]
    column = data.columns
    for col in column:
        if (data[col].dtype == 'int64') or  (data[col].dtype == 'float64'):
            quanti.append(col)
        else:
            quali.append(col)
    qualitative = train_data[quali]
    dataset= qualitative.values
    X = dataset[:, :-1]
    y = dataset[:,-1]
    X = X.astype(str)
    return X, y

X,y = load_dataset_quali(house_data)


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
plt.figure(figsize=(20,10))
plt.bar([i for i in range(len(fs.scores_))], fs.scores_)
plt.show()


#Selected features
train_selected = house_data[['House_age',
 'Remodeled', 'YearRemodAdd', 'YearBuilt', 'TotRmsAbvGrd', 'FullBath', '1stFlrSF',
 'TotalBsmtSF', 'GarageArea', 'GarageCars', 'TotalSF', 'OverallQual',
 'Neighborhood','BsmtQual','HeatingQC','KitchenQual','GarageFinish',
 'GarageType','SaleType', 'SalePrice']].iloc[0:1460]

test_selected = house_data[['House_age',
 'Remodeled', 'YearRemodAdd', 'YearBuilt', 'TotRmsAbvGrd', 'FullBath', '1stFlrSF',
 'TotalBsmtSF', 'GarageArea', 'GarageCars', 'TotalSF', 'OverallQual',
 'Neighborhood','BsmtQual','HeatingQC','KitchenQual','GarageFinish',
 'GarageType','SaleType', 'SalePrice']].iloc[1460:]

train_selected.to_csv('train_selected.csv')
test_selected.to_csv('test_selected.csv')
































