"""
NN to classify cancer

24/01/21

Victor
"""

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import f1_score



cancer = load_breast_cancer()
df = pd.DataFrame(np.c_[cancer['data'], cancer['target']],
                  columns= np.append(cancer['feature_names'], ['target']))

train = df[0:485]
test = df[len(train):]
print(train.shape, test.shape)

y_train = train['target'].values
y_train = y_train.reshape(-1,1)
train = train.drop('target', axis=1)
X_train = train.values

y_test = test['target'].values
y_test = y_test.reshape(-1,1)
test = test.drop('target', axis=1)
X_test = test.values


def sigmoid(x):
    return 1/ (1+ np.exp(-x))

def layers(X,y, n_hidden = 0 ):
    n_input = X.shape[0]
    n_hidden = n_hidden
    n_output = y.shape[0]
    return n_input,n_hidden,n_output


def initialize_parameters(n_input,n_hidden,n_output):
    W1 = np.random.randn(n_hidden,n_input) * 0.01
    b1 = np.zeros((n_hidden,1))
    W2 = np.random.randn(n_output,n_hidden) * 0.01
    b2 = np.zeros((n_output,1))

    parameters = {
    "W1":W1,
    "b1":b1,
    "W2":W2,
    "b2":b2
    }
    return parameters

def forward_prop(X, parameters):

    W1 = parameters['W1']
    b1 = parameters['b1']
    W2 = parameters['W2']
    b2 = parameters['b2']


    z1 = np.dot(W1,X) + b1
    a1 = np.tanh(z1)
    z2 = np.dot(W2,a1) + b2
    a2 = sigmoid(z2)

    cache = {"z1": z1,
             "a1": a1,
             "z2": z2,
             "a2": a2}
    return a2, cache

def cost_compute(a2, y):
    A2 = a2
    Y = y.reshape(-1,1)
    m = y.shape[0]
    logprobs = np.multiply(np.log(A2), Y) + np.multiply((1 - Y), np.log(1 - A2))
    cost = - np.sum(logprobs) / m

    cost = float(np.squeeze(cost))
    return cost

def backprop(parameters, cache, X, y):
    W1 = parameters['W1']
    b1 = parameters['b1']
    W2 = parameters['W2']
    b2 = parameters['b2']

    A1 = cache['a1']
    A2 = cache['a2']
    m=X.shape[0]

    dZ2 = A2 - y
    dW2 = 1/m * np.dot(dZ2,A1.T)
    db2 = 1/m * np.sum(dZ2, axis = 1, keepdims = True)
    dZ1 = np.dot(W2.T, dZ2)*(1 - np.power(A1, 2))
    dW1 = 1/m * np.dot(dZ1,X.T)
    db1 = 1/m * np.sum(dZ1, axis = 1, keepdims = True)

    grads = {"dW1": dW1,
             "db1": db1,
             "dW2": dW2,
             "db2": db2}

    return grads

def updatePara(parameters,grads, learning_rate = 0.02 ):
    W1 = parameters['W1']
    b1 = parameters['b1']
    W2 = parameters['W2']
    b2 = parameters['b2']

    dW1 = grads['dW1']
    db1 = grads['db1']
    dW2 = grads['dW2']
    db2 = grads['db2']

    W1 = W1 - learning_rate * dW1
    b1 = b1 - learning_rate * db1
    W2 = W2 - learning_rate * dW2
    b2 = b2 - learning_rate * db2

    parameters = {"W1": W1,
                  "b1": b1,
                  "W2": W2,
                  "b2": b2}
    return parameters

def model(X,y,n_hidden, num_iterations, learning_rate=1.2,print_cost=False):
    n_input,n_hidden,n_output = layers(X,y,n_hidden)

    parameters = initialize_parameters(n_input,n_hidden,n_output)

    for i in range(0,num_iterations):
        a2, cache = forward_prop(X,  parameters)
        cost = cost_compute(a2, y)

        grads = backprop(parameters, cache, X, y)

        parameters = updatePara(parameters, grads, learning_rate)

        if print_cost and i % 1000 == 0:
            print ("Cost after iteration %i: %f" %(i, cost))

    return parameters

parameters = model(X_train,y_train, n_hidden = 4,num_iterations = 10000,learning_rate=1.2,print_cost=True)
