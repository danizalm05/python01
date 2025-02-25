"""
66b-Applying various normalization methods in python
 ------------------------------------------- 
https://www.youtube.com/watch?v=0Vly0hajtLo&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=68
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial66b_various_data_normalization_techniques.py

db source:  housing = fetch_california_housing()
cloumn names 
  
0	MedInc
1	HouseAge
2	AveRooms
3	AveBedrms
4	Population
5	AveOccup
6	Latitude
7	Longitude
8	target
 """
 
 
import numpy as np
import cv2
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing()
 
#import 'housing into aata  frame
df = pd.DataFrame(data= np.c_[housing['data'], housing['target']],
                     columns= housing['feature_names'] + ['target'])

#df = pd.read_csv("data/normalization.csv")
print("\ndf.describe().T\n===========\n")
print(df.describe().T)
yttt = df.columns
#
#Define the dependent variable that
# needs to be predicted (labels) .
#the target column is the price of the house
Y = df["target"].values


#Define the independent variables. All the column 
#except traget, beacuse this is the prediction.
X = df.drop(labels = ["target"], axis=1) 


sns.distplot(df['MedInc'], kde=False)
plt.show()
sns.distplot(df['AveOccup'], kde=False) # Large Outliers. 1243 occupants?
plt.show()
sns.distplot(df['Population'], kde=False) #Outliers. 35682 max but mean 1425

plt.show()

X = X[['MedInc', 'AveOccup']].copy()#only this two cloumns
column_names = X.columns

#sns.jointplot(x='MedInc', y='AveOccup', data=X, xlim=[0,10], ylim=[0,5] ) # xlim=[0,10], ylim=[0,5]
#plt.show()



from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import PowerTransformer
from sklearn.preprocessing import QuantileTransformer

#Other transformations not shown below. 
from sklearn.preprocessing import minmax_scale
from sklearn.preprocessing import MaxAbsScaler
from sklearn.preprocessing import Normalizer

##############################################################################
from sklearn.preprocessing import StandardScaler
#1 Standard scaler
#removes the mean and scales the data to unit variance.
# But, outliers have influence when computing mean and std. dev.
scaler1 = StandardScaler()
scaler1.fit(X)
X1 = scaler1.transform(X)
df1 = pd.DataFrame(data=X1, columns=column_names)
print(df1.describe())
sns.jointplot(x='MedInc', y='AveOccup', data=df1)  #Data scaled but outliers still exist
plt.suptitle("Standard scaler")
 
plt.show()

#13:30


####################################
#2 MinMaxScaler##########################################