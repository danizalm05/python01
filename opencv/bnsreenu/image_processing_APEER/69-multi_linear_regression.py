"""
69-multi_linear_regression.py
 -------------------------------------------
https://www.youtube.com/watch?v=9CxJhQynU20&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=70https://www.youtube.com/watch?v=_gTr5DtndeU&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=71
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial69-multi_linear_regression.py
 
Multiple Linear Regression uses several explanatory 
variables to predict the outcome of a response variable.

There are a lot of variables and multiple linear 
regression is designed to create a model 
based on all these variables. 

#Dataset link:
https://cdn.scribbr.com/wp-content/uploads//2020/02/heart.data_.zip?_ga=2.217642335.893016210.1598387608-409916526.1598387608
  csv head line  "","biking","smoking","heart.disease"

#Heart disease
The effect that the independent variables biking and 
smoking (two  varibles) have on the dependent variable heart disease 

"""

import pandas as pd
import seaborn as sns
import numpy as np

df = pd.read_csv('data/heart_data.csv')
#print(df.head())

df = df.drop("Unnamed: 0", axis=1)#Drop the first column
print(df.head())

#A few plots in Seaborn to understand the data 
sns.lmplot(x='biking', y='heart.disease', data=df)  
sns.lmplot(x='smoking', y='heart.disease', data=df)  


x_df = df.drop('heart.disease', axis=1)
y_df = df['heart.disease']


from sklearn import linear_model

#Create Linear Regression object
model = linear_model.LinearRegression()

#Now let us call fit method to train the model using independent variables.
#And the value that needs to be predicted (Images_Analyzed)
 

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x_df, y_df, test_size=0.3, random_state=42)

model.fit(X_train, y_train) #Indep variables, dep. variable to be predicted

#Prints the R^2 value, a measure of how well
print("\nR^2 value = ",model.score(X_train, y_train))  
#08:00
