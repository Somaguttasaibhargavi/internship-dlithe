# -*- coding: utf-8 -*-
"""tennisplayerdataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IbeBnH9tImv9dH1Kbi2O_wlOnDTAAYbP
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

from google.colab import files ##upload the downloaded 193_799887_compressed_Data.csv.zip  file 
uploaded = files.upload()

tennis=pd.read_csv('193_799887_compressed_Data.csv.zip',header=0,encoding='ISO-8859-1')

tennis

plt.figure(figsize=(10,10))
sns.heatmap(tennis.isnull(),yticklabels=False,cbar=False,cmap='viridis')

plt.figure(figsize=(10,10))
sns.heatmap(tennis.corr())

plt.figure(figsize=(20,10))
sns.heatmap(tennis.isnull(),yticklabels=False,cbar=False,cmap='viridis')

tennis.describe()

tennis.isnull().sum()

Surface=pd.get_dummies(tennis['Surface'],drop_first=True)
Tournament=pd.get_dummies(tennis['Tournament'],drop_first=True)
Winner=pd.get_dummies(tennis['Winner'],drop_first=True)
Loser=pd.get_dummies(tennis['Loser'],drop_first=True)

tennis.drop(['Surface','Tournament','Winner','Loser'],axis=1,inplace=True)

tennis

tennis=pd.concat([tennis,Surface,Tournament,Winner,Loser],axis=1)

tennis

pd.options.display.max_columns=None #to display all columns
display(tennis.head())

tennis.info()

import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

imputer

"""# Data Cleaning"""

tennis.ATP=tennis.ATP.fillna(tennis['ATP'].mean())
tennis.Location=tennis.Location.fillna(30)
tennis.Series=tennis.Series.fillna(30)
tennis.Court=tennis.Court.fillna(30)
tennis.Wsets=tennis.Wsets.fillna(tennis['Wsets'].median())
tennis.Lsets=tennis.Lsets.fillna(tennis['Lsets'].median())
tennis.Round=tennis.Round.fillna(30)
tennis.WRank=tennis.WRank.fillna(30)
tennis.LRank=tennis.LRank.fillna(30)
tennis.W1=tennis.W1.fillna(tennis['W1'].median())
tennis.L1=tennis.L1.fillna(tennis['L1'].median())
tennis.W2=tennis.W2.fillna(tennis['W2'].median())
tennis.L2=tennis.L2.fillna(tennis['L2'].median())
tennis.W3=tennis.W3.fillna(tennis['W3'].median())
tennis.L3=tennis.L3.fillna(tennis['L3'].median())
tennis.W4=tennis.W4.fillna(tennis['W4'].median())
tennis.L4=tennis.L4.fillna(tennis['L4'].median())
tennis.W5=tennis.W5.fillna(tennis['W5'].median())
tennis.L5=tennis.L5.fillna(tennis['L5'].median())
tennis.Comment=tennis.Comment.fillna(30)

plt.figure(figsize=(20,10))
sns.heatmap(tennis.isnull(),yticklabels=False,cbar=False,cmap='viridis')

fig=plt.subplots(figsize=(20,15))
plt.subplot(6,4,1)
plt.hist(tennis['Location'])
plt.title('location')
plt.subplot(6,4,2)
plt.hist(tennis['ATP'])
plt.title('ATP')
plt.subplot(6,4,3)
plt.hist(tennis['Date'])
plt.title('date')
plt.subplot(6,4,4)
plt.hist(tennis['Series'])
plt.title('Series')
plt.subplot(6,4,5)
plt.hist(tennis['Court'])
plt.title('Court')
plt.subplot(6,4,6)
plt.hist(tennis['Comment'])
plt.title('Comment')
plt.subplot(6,4,7)

plt.figure(figsize=(20,10))
sns.heatmap(tennis.isnull(),yticklabels=False,cbar=False,cmap='viridis')



"""# For Winner_Id"""

pair1=tennis[['ATP','Best of','WRank','W1','W2','Wsets']]
sns.pairplot(pair1)

sns.jointplot(x='W1',y='W2',data=tennis,kind='reg')

sns.jointplot(x='W1',y='L1',data=tennis,kind='reg')

sns.jointplot(x='Wsets',y='Lsets',data=tennis,kind='reg')

sns.jointplot(x='W3',y='L3',data=tennis,kind='reg')

sns.jointplot(x='W2',y='L2',data=tennis,kind='reg')

sns.jointplot(x='W4',y='L4',data=tennis,kind='reg')

sns.jointplot(x='W5',y='L5',data=tennis,kind='reg')

sns.jointplot(x='W1',y='W3',data=tennis,kind='reg')

sns.jointplot(x='W1',y='W4',data=tennis,kind='reg')

sns.jointplot(x='W1',y='W5',data=tennis,kind='reg')

sns.jointplot(x='W2',y='W3',data=tennis,kind='reg')

sns.jointplot(x='W2',y='W5',data=tennis,kind='reg')

sns.jointplot(x='W3',y='W5',data=tennis,kind='reg')

x1=tennis[['WRank','LRank','W1','L1','W2','L2','W3','L3','W4','L4','W5','L5','Wsets','Lsets']]
y1=tennis['ATP']

from keras.datasets import cifar10

(x_train, y_train), (x_test, y_test) = cifar10.load_data()
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')

print('y_train shape', y_train.shape)
print(x_test.shape[0], 'test samples')

print('x_test shape', x_test.shape)
print(y_test.shape[0], 'test samples')

"""#Logistic Regression"""

!pip install keras

from keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()

import tensorflow as tf
import numpy as np
import os

import distutils
if distutils.version.LooseVersion(tf.__version__) <= '2.0':
    raise Exception('This notebook is compatible with TensorFlow 1.14 or higher, for TensorFlow 1.13 or lower please use the previous version at https://github.com/tensorflow/tpu/blob/r1.13/tools/colab/fashion_mnist.ipynb')

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()

# add empty color dimension
X_train = np.expand_dims(X_train, -1)
X_test = np.expand_dims(X_test, -1)

mnist = tf.keras.datasets.mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_train, X_test = X_train / 300.0, X_test / 300.0
X_test = X_test.reshape(X_test.shape[0], -1)
X_train = X_train.reshape(X_train.shape[0], -1)

import sklearn.linear_model as sk
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
logmodel=LogisticRegression()
logmodel.fit(X_train,y_train)
predictions=logmodel.predict(X_test)

from sklearn.metrics import classification_report
print(classification_report(y_test,predictions))

print(confusion_matrix(y_test,predictions))



"""# K-Nearest Neighbors"""

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)
pred=knn.predict(X_test)
from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(y_test,pred))

print(classification_report(y_test,predictions))

error_rate=[]
for i in range(1,20):
  knn=KNeighborsClassifier(n_neighbors=1)
  knn.fit(X_train,y_train)
  pred_i=knn.predict(X_test)
  error_rate.append(np.mean(pred_i!=y_test))
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.plot(range(1,20),error_rate,color='blue',linestyle='dashed',markers='o',markerfacecolor='red',markersize=10)
plt.title('error rate vs k value')
plt.xlabel('error rate')

knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,y_train)
pred=knn.predict(X_test)
print(connfusion_matrix(y_test,pred))

from sklearn.metrices import classification_report
print(classification_report(y_test,pred))



"""# KNaive Bayes"""

from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)

print(classification_report(y_test,y_pred))

