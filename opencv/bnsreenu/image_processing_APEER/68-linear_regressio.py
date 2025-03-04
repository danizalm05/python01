"""
tutorial68-linear_regression.py
 -------------------------------------------
https://www.youtube.com/watch?v=9CxJhQynU20&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=70
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial68-linear_regression.py

db source:
https://github.com/bnsreenu/python_for_microscopists/blob/master/other_files/cells.csv



pip3 install pandas

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/cells.csv')
print(df)
plt.scatter(x="time", y="cells", data=df)
plt.show()


#Now let us define our x and y values for the model.
#x values will be time column, so we can define it by
# dropping cells
#

#y will be cells column, dependent variable that we are 
#trying to predict. 

x_df = df.drop('cells', axis='columns')

#Or you can pick columns manually. 
#
#   Single bracket returns as series
#   double returns pandas dataframe which is what the model 
#expects.
#x_df=df[['time']]
 
print("x_df.dtypes =  ",x_df.dtypes) 
#Prints as object when you drop cells or use double brackets [[]]
#Prints as float64 if you do only single brackets,
# which is not the right type for our model. 
y_df = df.cells
 

#SPlit data into training and test datasets so
# we can validate the model using test data
# 08:04
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = \
      train_test_split(x_df, y_df, test_size=0.3, random_state=42)
#random_state can be any integer and it is used as a seed to
# randomly split dataset.
#By doing this we work with same test dataset evry time, 
#if this is important.
#random_state=None splits dataset randomly every time

#-----------------------------------------------------------
#       Y =   the value we want to predict
#       X = all independent variables upon which Y depends. 
#  steps for linear regression....
# Step 1:   Create the instance of the model
# Step 2:   .fit() to train the model or fit a linear model
# Step 3:   .predict() to predict Y for given X values. 
# Step 4:   Calculate the accuracy of the model. 

#TO create a model instance 
from sklearn import linear_model
model = linear_model.LinearRegression()  #Create an instance of the model.
model.fit(X_train, y_train)   #Train the model or fits a linear model

print("model.score(X_train, y_train) = ",model.score(X_train, y_train))  #Prints the R^2 value, a measure of how well
#observed values are replicated by themodel. 


prediction_test = model.predict(X_test)    
print("\ny_test \n ------- \n",y_test )
print("\nprediction_tes  = ", prediction_test)

print("\nMean sq. errror between y_test and predicted =", np.mean(prediction_test-y_test)**2)
# A MSE value of about 8 is not bad compared to average # cells about 250.


#Residual plot
plt.scatter(prediction_test, prediction_test-y_test)
plt.hlines(y=0, xmin=200, xmax=300)# just draw the y=0 axis
plt.show()
#Plot would be useful for lot of data points