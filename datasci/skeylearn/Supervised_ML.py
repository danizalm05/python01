'''
 # Supervised Machine Learning - Part 1

You are a real estate analysts, and requested to analyze data of apartments
that were sold in Melbourne (Australia.
All the data is stored in a file named `melb_data.csv` in the `data`
sub folder. Your end goal is two fold:
1. Build a model to predict if a given aparment has more then 3 bedrooms
  or not.
2. Build a model to predict the estimated price for a given apartment

      https://scikit-learn.org/stable/glossary.html#glossary
      https://en.wikipedia.org/wiki/Logistic_regression


'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

# Load the `melb_data.csv` data source (Melbourne housing prices)
df = pd.read_csv('./data/melb_data.csv', index_col=0)  # load data
print(df.head(10))

'''
Column name in the csv file
Suburb,Address,Rooms,Type,Price,Method,SellerG,Date,Distance,Postcode,
Bedroom2,Bathroom,Car,Landsize,BuildingArea,YearBuilt,CouncilArea,
Lattitude,Longtitude,Regionname,Propertycount

'''
# initial description of the data
# numeric values
print("\n\ndf.describe()\n--------------\n", df.describe())
# All  values
print("\n\ndf.describe(all)\n--------------\n", df.describe(include='all'))

print("\nMissing values\n-------\n ", df.isnull().sum())

# Accorrding the above result there many missing values so we sould drop
# some of them

'''
Bedroom2  Bathroom  Car  Landsize   BuildingArea   YearBuilt  CouncilArea       6163
Lattitude  Longtitude
'''
df.drop(["BuildingArea", "YearBuilt", "CouncilArea"], axis=1, inplace=True)
print("\nMissing values after first drop\n-------\n ", df.isnull().sum())
df.dropna(inplace=True)
print("\nMissing values after 2'nd drop\n-------\n ", df.isnull().sum())

print("\n\n2'nd df.describe()\n--------------\n", df.describe())
# 6.34
'''
build a model to predict if an apartment has less than 3 rooms or not.
Do you need to do any pre-processing on the data?
What algorithm do you chose?
'''
# We need to add a column that indicates if the house has than 3 rooms
df["has3bedromms"] = df["Rooms"] >= 3
print("\n\nhas3bedromms\n--------------\n", df)
# Drop the "Rooms" column
is3Rooms = df.drop(["Rooms"], axis=1)
print("\n\nis3Rooms\n--------------\n", df)
# 8.45
print("\ncolumns  list =", is3Rooms.columns)
'''
columns  list = Index(['Suburb', 'Address', 'Type', 'Price', 'Method',
        'SellerG', 'Date',
       'Distance', 'Postcode', 'Bedroom2', 'Bathroom', 'Car', 
       'Landsize',
       'Lattitude', 'Longtitude', 'Regionname', 'Propertycount',
       'has3bedromms'],
'''
# Drop cloumns that we don't need
is3Rooms.drop(['Suburb', 'Address', 'Type', 'Method', 'SellerG', 'Date',
               'Regionname', ], axis=1, inplace=True)
# 'inplace=True' will change the original data frame
print("\nis3Rooms  list \n--------------\n", is3Rooms)

from sklearn.model_selection import train_test_split
from sklearn import metrics, preprocessing
from sklearn.linear_model import LinearRegression, LogisticRegression

# 11:56
xtrain, xtest, ytrain, ytest = \
    train_test_split(
        is3Rooms.drop("has3bedromms", axis=1),
        is3Rooms["has3bedromms"], random_state=0)
# train_test_split(X, y,random_state = 0 )
# 12:36
print(" ytrain \n------------\n", ytrain)
clf = LogisticRegression()
clf.fit(xtrain, ytrain)
acc = clf.score(xtest, ytest)
print("accurace = ", acc)
###   Second  question
'''
Build a model to predict the price of a house you have not seen before.
0:25
'''
# from sklearn.linear_model import LinearRegression

df4reg = df.drop(['Suburb', 'Address', 'Type', 'Method', 'SellerG', 'Date',
                  'Regionname', 'has3bedromms'], axis=1)  # Drop categorical variables
from sklearn.preprocessing import LabelEncoder

''' LabelEncoder().fit_transform(df["Suburb"]):
           Encode target labels with value between 0 and n_classes-1.
           This transformer should be used to encode target 
           values, i.e. y, and not the input X.
'''
df4reg["Suburb"] = LabelEncoder().fit_transform(df["Suburb"])
df4reg["Address"] = LabelEncoder().fit_transform(df["Address"])
df4reg["Type"] = LabelEncoder().fit_transform(df["Type"])
df4reg["Method"] = LabelEncoder().fit_transform(df["Method"])
df4reg["SellerG"] = LabelEncoder().fit_transform(df["SellerG"])
df4reg["Date"] = LabelEncoder().fit_transform(df["Date"])
df4reg["Regionname"] = LabelEncoder().fit_transform(df["Regionname"])
# move the price column to the right
df4reg = df4reg[['Suburb', 'Address', 'Type', 'Method', 'SellerG', 'Date',
                 'Regionname', 'Rooms', 'Distance', 'Postcode', 'Bedroom2', 'Bathroom', 'Car',
                 'Landsize', 'Lattitude', 'Longtitude', 'Propertycount', 'Price']]

# print(" df4reg \n------------\n" ,df4reg)
# print(" df4reg.column = " ,df4reg.columns)
# 2:26
X = df4reg.iloc[:, :-1]  # all columns without the right most column
y = df4reg.iloc[:, -1]  # only the  right most column - 'Price'

xtrain2, xtest2, ytrain2, ytest2 = train_test_split(X, y, random_state=0)

reg = LinearRegression(fit_intercept=False)
reg.fit(xtrain2, ytrain2)
y_pred = reg.predict(xtest2)
print("\n y_pred\n -----------\n ", y_pred)
# Now we measure the performance
# 5:30

print(f"mae: {metrics.mean_squared_error(ytest2, y_pred)}")  # this result doesn't mean a lot
print(f"r^2: {metrics.r2_score(ytest2, y_pred)}")
# The r^2 above is less than 0.5 and this is not so good.
# So we need to improve the model
# One way is to use the categorical variables that we dropped.

# 6:48
'''
would different parametrs or algorithms provide different results?
compre some of the algorithms.
Do analysis of the most significant factors that have impact on the price?
'''
#12:06
abs_dfreg = abs(reg.coef_)
zip_dfreg = zip(df4reg.columns,abs_dfreg)
dict_dfreg = dict(zip_dfreg) #for each var write the cofficent

sorted_dfreg = sorted(dict_dfreg.items(), key = lambda x:x[1], reverse = True)
# Sort the dict according to the abs value of cofficent weight in revers order
print("\n ----  sorted_dfreg table ------\n ------------------------------\n " )
for k,v in sorted_dfreg :
   print(k,v)
#according to the result the vlaues Lattitude,  Longtitude,  Type are the most importent
#14:30  is3Rooms
abs_is3Rooms = abs(clf.coef_[0])


zip_is3Rooms = zip(is3Rooms.columns,abs_is3Rooms)

dict_is3Rooms = dict(zip_is3Rooms) #for each var write the cofficent

sorted_is3Rooms = sorted(dict_is3Rooms.items(), key = lambda x:x[1], reverse = True)
print("\n ----  sorted_is3Rooms ------\n ------------------------------\n " )
for k,v in sorted_is3Rooms :
   print(k,v)








