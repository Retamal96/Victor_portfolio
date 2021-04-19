# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 11:23:09 2021

@author: victo
"""
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns





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
missing = house_data.isna().sum().reset_index()

dff = house_data.copy()

def col_types(df):
    num_cols = df.loc[:, df.dtypes != "object"].columns.tolist()
    cat_cols = df.loc[:, df.dtypes == "object"].columns.tolist()
    ord_cols = []
    for col in num_cols:
        if df[col].value_counts().size < 20:
            ord_cols.append(col)

    num_cols = [x for x in num_cols if x not in ord_cols + ["Id", "SalePrice"]]
    
    return num_cols, cat_cols, ord_cols

num_cols, cat_cols, ord_cols = col_types(dff)

for col in dff.columns:
    print("For column: ", col + "\n")
    print(dff[col].value_counts(), "\n")



def bar_box(df, col, target = "SalePrice"):
    
    sns.set_style("darkgrid")
    fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharex = True)
    
    order = sorted(df[col].unique())
    
    sns.countplot(data = df[df[target].notnull()], x = col, ax = axes[0], order = order)    
    sns.countplot(data = df[df[target].isnull()], x = col, ax = axes[1], order = order)    
    sns.boxplot(data = df, x = col, ax = axes[2], y = target, order = order)
    
    fig.suptitle("For Feature:  " + col)
    axes[0].set_title("in Training Set ")
    axes[1].set_title("in Test Set ")
    axes[2].set_title(col + " --- " + target)
    
    for ax in fig.axes:
        plt.sca(ax)
        plt.xticks(rotation=90)

bar_box(house_data,'MasVnrArea')


def plot_scatter(df, col, target = "SalePrice"):
    sns.set_style("darkgrid")
    
    corr = df[[col, target]].corr()[col][1]    
    c = ["red"] if corr >= 0.7 else (["brown"] if corr >= 0.3 else\
                                    (["lightcoral"] if corr >= 0 else\
                                    (["blue"] if corr <= -0.7 else\
                                    (["royalblue"] if corr <= -0.3 else ["lightskyblue"]))))    

    fig, ax = plt.subplots(figsize = (5, 5))
    
    sns.scatterplot(x = col, y = target, data = df, c = c, ax = ax)        
    ax.set_title("Correlation between " + col + " and " + target + " is: " + str(corr.round(4)))

def feature_distribution(df, col, target = "SalePrice", test = True):
    sns.set_style("darkgrid")
    if test == True:
        fig, axes = plt.subplots(1, 5, figsize=(25, 5))

        sns.kdeplot(data = df[df[target].notnull()], x = col, fill=True, label = "Train", ax = axes[0], color = "orangered")
        sns.kdeplot(data = df[df[target].isnull()], x = col, fill=True, label = "Test", ax = axes[0], color = "royalblue")
        axes[0].set_title("Distribution")
        axes[0].legend(loc = "best")
        
        sns.boxplot(data = df[df[target].notnull()], y = col, ax = axes[1], color = "orangered")
        sns.boxplot(data = df[df[target].isnull()], y = col, ax = axes[2], color = "royalblue")
        axes[2].set_ylim(axes[1].get_ylim())        
        axes[1].set_title("Boxplot For Train Data")
        axes[2].set_title("Boxplot For Test Data")
        

        stats.probplot(df[df[target].notnull()][col], plot = axes[3])
        stats.probplot(df[df[target].isnull()][col], plot = axes[4])
        axes[4].set_ylim(axes[3].get_ylim())        
        axes[3].set_title("Probability Plot For Train data")
        axes[4].set_title("Probability Plot For Test data")
        
        fig.suptitle("For Feature:  " + col)
    else:
        fig, axes = plt.subplots(1, 3, figsize = (18, 6))
        
        sns.kdeplot(data = df, x = col, fill = True, ax = axes[0], color = "orangered")
        sns.boxplot(data = df, y = col, ax = axes[1], color = "orangered")
        stats.probplot(df[col], plot = axes[2])
        
        axes[0].set_title("Distribution")
        axes[1].set_title("Boxplot")
        axes[2].set_title("Probability Plot")
        fig.suptitle("For Feature:  " + col)








