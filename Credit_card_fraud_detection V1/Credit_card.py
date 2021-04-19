"""
Credit card fraud detection
"""

import pandas as  pd
import matplotlib.pyplot as plt
import seaborn as sns


card_data = pd.read_csv(r'C:\Users\victo\Desktop\Datascience\Projects\Programming exercises\Credit_cards\creditcard.csv')

card_data.head()

len(card_data)

card_data.shape

card_data = card_data.sample(frac=0.2, random_state= 1)

#card_data.hist(figsize = (20,20))

card_data['Class'].unique()

Fraud = card_data[card_data['Class'] == 1]

Normal = card_data[card_data['Class'] == 0]

## LOOKING AT THE OUTLIER FRACTION

outlier = len(Fraud) / float(len(Normal))

print('There are {} outliers'.format(outlier))
print('There are {} Frauds'.format(len(Fraud)))
print('There are {} Normal'.format(len(Normal)))

"""corrmat = card_data.corr()
fig = plt.figure(figsize = (12, 9))"""

#sns.heatmap(corrmat, vmax = .8, square = True)

"""
Organizing the data to start

"""
columns = card_data.columns.tolist()

columns = [c for c in columns if c not in ['Class']]
columns2 = [ c for c in columns if c != 'Class']
target = 'Class'
X = card_data[columns]
print(X.shape)
y = card_data[target]
print(y.shape)


"""
Algorithms

"""
from sklearn.metrics import classification_report, accuracy_score
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

state= 1
classifiers = {
    'Isolation Forest' : IsolationForest(max_samples=len(X),
                                         contamination = outlier,
                                         random_state = state),
    'Local Outlier Factor': LocalOutlierFactor( n_neighbors = 20,
                                               contamination = outlier)
    }

#### FIT the model ####

n_outliers = len(Fraud)

for i, (clf_name, clf) in enumerate(classifiers.items()):

    # fit the data and tag outliers
    if clf_name == 'Local Outlier Factor':
        y_pred = clf.fit_predict(X)
        scores_pred = clf.negative_outlier_factor_
    else:
        clf.fit(X)
        scores_pred = clf.decision_function(X)
        y_pred = clf.predict(X)

 # reshape the prediction values to 0 for valid and 1 for fraud
    y_pred[y_pred == 1] = 0
    y_pred[y_pred == -1] = 1

    # calculate the number of errors
    n_errors = (y_pred != y).sum()


        # classification matrix
    print('{}: {}'.format(clf_name, n_errors))
    print(accuracy_score(y, y_pred))
    print(classification_report(y, y_pred))
