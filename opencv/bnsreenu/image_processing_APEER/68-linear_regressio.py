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