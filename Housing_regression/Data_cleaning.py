# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 12:18:44 2021

@author: victo
"""

import pandas as pd
import numpy as np

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

house_data = pd.concat([train, test], 
                       keys = ['train', 'test'], axis=0)

house_data.head()

house_data.info()
house_data.columns

## DEALING WITH MISSING VALUES 

missing = house_data.isna().sum().reset_index()
missing = missing[missing[0] > 1] 

house_data.loc[(house_data.MSZoning.isnull()) & (house_data.Neighborhood == "IDOTRR"), "MSZoning"] = "C (all)"
house_data.loc[(house_data.MSZoning.isnull()) & (house_data.Neighborhood == "Mitchel"), "MSZoning"] = "RL"

house_data.groupby('Street')['LotFrontage'].mean()

def Fill_with_mean(row):
    if row['Street'] == 'Grvl':
        return 88.2
    if row['Street'] == 'Pave':
        return 69.227817

house_data['LotFrontage'] = house_data.apply(lambda x: Fill_with_mean(x), axis = 1)

house_data.groupby('MasVnrType')['MasVnrArea'].mean()

def Ms_filler(row):
    if np.isnan(row['MasVnrArea']):
        if row['MasVnrType']== 'BrkCmn':
            return 195.48
        if row['MasVnrType'] == 'BrkFace':
            return 261.67
        if row['MasVnrType'] == 'None':
            return 0.8
        if row['MasVnrType'] == 'Stone':
            return 239.55
    else:
        return row['MasVnrArea']

house_data['MasVnrArea'] = house_data.apply(lambda x: Ms_filler(x), axis = 1)

house_data['BsmtUnfSF'] = house_data['BsmtUnfSF'].fillna(0)
house_data['BsmtFullBath'] = house_data['BsmtFullBath'].fillna(0)
house_data['BsmtHalfBath'] = house_data['BsmtHalfBath'].fillna(0)

house_data[['BsmtFinType1', 'BsmtFinType2']] = house_data[['BsmtFinType1', 'BsmtFinType2']].fillna('Unf')

house_data.groupby('BsmtFinType2')['BsmtFinSF2'].mean()
house_data.groupby('BsmtFinType1')['BsmtFinSF1'].mean()
def BstmFinSF1_NA(row):
    if np.isnan(row['BsmtFinSF1']):
        if row['BsmtFinType1']== 'ALQ':
            return 621.051282
        if row['BsmtFinType1'] == 'BLQ':
            return 527.732342
        if row['BsmtFinType1'] == 'GLQ':
            return 808.012956
        if row['BsmtFinType1'] == 'LwQ':
            return 387.064935
        if row['BsmtFinType1'] == 'Rec':
            return 465.524306
        if row['BsmtFinType1'] == 'Unf':
            return 0.000000
    else:
        return row['BsmtFinSF1']

house_data['BsmtFinSF1'] = house_data.apply(lambda x: BstmFinSF1_NA(x), axis = 1)

def BstmFinSF2_NA(row):
    if np.isnan(row['BsmtFinSF2']):
        if row['BsmtFinType2']== 'ALQ':
            return 621.051282
        if row['BsmtFinType2'] == 'BLQ':
            return 527.732342
        if row['BsmtFinType2'] == 'GLQ':
            return 808.012956
        if row['BsmtFinType2'] == 'LwQ':
            return 387.064935
        if row['BsmtFinType2'] == 'Rec':
            return 465.524306
        if row['BsmtFinType2'] == 'Unf':
            return 0.000000
    else:
        return row['BsmtFinSF2']

house_data['BsmtFinSF2'] = house_data.apply(lambda x: BstmFinSF2_NA(x), axis = 1)

tt = house_data[house_data['GarageCars'].isna() == True]

house_data.groupby('GarageType')['GarageYrBlt'].count()
house_data['GarageType'] = house_data['GarageType'].fillna('Unbuilt')

house_data.groupby('GarageType')['GarageYrBlt'].mean()
def Garage_fill(row):
    if row['GarageType'] == 'Unbuilt':
        return 0
    if row['GarageType'] == 'Detchd':
        return 1961
    else:
        return row['GarageYrBlt']
    
house_data['GarageYrBlt'] = house_data.apply(lambda x: Garage_fill(x), axis = 1 )

house_data[['GarageCars','GarageArea']] = house_data[['GarageCars','GarageArea']].fillna(0)


house_data[['Utilities','Alley', 'MasVnrType', 'BsmtQual', 'Fence', 'FireplaceQu', 'MiscFeature', 'PoolQC', 'BsmtCond', 'BsmtExposure','Electrical' ,'GarageQual', 'GarageCond','KitchenQual']] = house_data[['Utilities','Alley', 'MasVnrType', 'BsmtQual', 'Fence', 'FireplaceQu', 'MiscFeature', 'PoolQC', 'BsmtCond', 'BsmtExposure','Electrical', 'GarageQual', 'GarageCond','KitchenQual']].fillna('None') 
house_data['Utilities'] = house_data['Utilities'].fillna('AllPub')
house_data['Functional'] = house_data['Functional'].fillna('Typ')

corrs = house_data.corr()

house_data[['GarageFinish', 'GarageQual']] = house_data[['GarageFinish','GarageQual']].fillna('Unf')

house_data['SaleType'] = house_data['SaleType'].fillna('Oth')
house_data[['Exterior1st','Exterior2nd']] = house_data[['Exterior1st','Exterior2nd']] .fillna('None')


house_data[(house_data.Neighborhood == "IDOTRR") &  (house_data.OverallQual < 5) & (house_data.YearRemodAdd < 1960) & (house_data.ExterQual == "Fa")].Functional.value_counts()

missing = house_data.isna().sum().reset_index()
missing = missing[missing[0] > 1] 

"""
THE MISSING VALUES ARE DONE, THE ONLY ONE IS FUNCTIONAL. CHECK THIS OUT BEFORE MOVING ON. 

NEXT STEP WOULD BE FEATURE ENGENEERING

"""

house_data['House_age'] = house_data['YrSold'] - house_data['YearBuilt'] 

house_data['Remodeled'] = house_data['YrSold'] - house_data['YearRemodAdd']

house_data['TotalBsmtSF'] = house_data['BsmtFinSF1']  + house_data['BsmtFinSF2'] + house_data['BsmtUnfSF']

house_data['TotalSF'] = house_data['1stFlrSF']  + house_data['2ndFlrSF']

house_data['TotalPorch'] = house_data['OpenPorchSF'] + house_data['EnclosedPorch'] + house_data['3SsnPorch'] + house_data['ScreenPorch']

def exterior(row):  #check if more than one exterior material covering
    if row['Exterior1st'] == row['Exterior2nd']:
        return 1
    else:
        return 2 
    
house_data['number_of_exteriors'] = 0
house_data['number_of_exteriors'] = house_data.apply(lambda row: exterior(row), axis = 1)

def redundant_exterior(row):  #second second column to none if same as first exterior
    if row['Exterior1st'] == row['Exterior2nd']:
        row['Exterior2nd'] = 'None'
    else:
        row['Exterior2nd'] =  row['Exterior2nd']
    return row['Exterior2nd']

house_data['Exterior2nd'] = house_data.apply(lambda row: redundant_exterior(row), axis = 1)

house_data.drop(['GrLivArea'], axis = 1, inplace=True)

house_data.to_csv('data_clean.csv')

house_data.columns
