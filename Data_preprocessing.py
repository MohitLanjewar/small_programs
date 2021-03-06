import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
dataset = pd.read_csv('Data.csv')

#importing dataset
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values

#taking care of mssing dataset
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(x[:,1:3])
 
# Imputing the data    
x[:,1:3] = imputer.transform(x[:,1:3])
x

#encoding categorial data into numeric data (label encoder class is used to transform ctegorical data into numeric data)
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
x[:,0]=le.fit_transform(x[:,0])

#OneHotEncoder is used to transform that categorical data into further columns
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
x = ct.fit_transform(x)
