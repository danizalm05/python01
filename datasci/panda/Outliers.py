#!/usr/bin/env python3
'''

 Taking care of data Outliers

https://courses.campus.gov.il/courses/course-v1:HIT+ACD_RFP4_DataScienceIntro_HE+2022_1/courseware/0f960b9a58644ff4b9c375b0624f8d18/14bbbe4680304e278e6b563ee4c6ac66/?child=first
https://labs.vocareum.com/main/main.php?m=editor&asnid=537352&stepid=537353&hideNavBar=1

'''


import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
#%matplotlib inline
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('data/titanic.csv', header=0, sep=',')
print(df.describe(include='all') )
print("df.Age.describe()\n--------------\n" )
print(df.Age.describe() )
               #There 2  ways to find outliers
#1. Using graph to find outliers
plt.hist(df.Fare, bins=50)
plt.xlabel=("Fare")
plt.ylabel=("Frequency")
plt.show()



#Using  values to find outliers
# If we define outliers values for 'Fare' as values bigger then 200
outliersValue = 200
numOfOutliers = sum(df.Fare>outliersValue)# numcer of 'Fare' outliers
print("Number Of 'Fare' Outliers = ",numOfOutliers)

# 2.Using the distance   from the median
import seaborn as sns
#presented boxplot shows the minimum, maximum, 1st quartile and 3rd quartile.

sns.boxplot(x=df.Age,palette="Blues")
plt.show()
# using Interquartile range  to find outliers
Q1 = np.percentile(df["Fare"], 25)
Q3 = np.percentile(df["Fare"], 75)
IQR = Q3 - Q1
print("Q1 = ",Q1,"  Q3 =",Q3,"IQR => Q3 - Q1 = ", IQR )
#6:55
smallOutlier = (df["Fare"] < Q1 - 1.5*IQR) #True for evry outlier
print("smallOutlier \n----------\n ", smallOutlier)
highOutlier = (df["Fare"] > Q3 + 1.5*IQR)#True for evry outlier
print("highOutlier \n----------\n ", highOutlier)

# Find index of al the outlier
Fare_outlier_rows = df[(smallOutlier) | (highOutlier )].index
print("len(Fare_outlier_rows) = ",len(Fare_outlier_rows))

#Scan two cloumn togther
mycols = ["Age","Fare"]# outlier in cloumn "age" or cloumn "Fare"

all_outlier_rows = []# A list that will keep all indexs of of the two column
for col in mycols:
    Q1 = np.percentile(df[col], 25)
    Q3 = np.percentile(df[col], 75)
    IQR = Q3 - Q1
    IQR_range = 1.5 * IQR
    smallOutlier = (df[col] < Q1 - IQR_range)
    highOutlier =  df[col] > Q3 + IQR_range#True for evry outlier
    col_outlier = df[  smallOutlier | highOutlier  ].index

    all_outlier_rows.extend(col_outlier)
    # The above list might contain duplicate outlier
#8:00
print("len(all_outlier_rows) = ",len(all_outlier_rows))
'''
A set is a collection of unordered values or items. The set in python 
has similar properties to the set in mathematics. 
Important features of set in python:
 A set in python is an iterable object.
A set in python does not contain duplicate values.
'''
#Print number of non duplicat items
print("len(set(all_outlier_rows)) " ,len(set(all_outlier_rows)))
#8:42

#3. using stadart deviation  to find outliers

# We wll use the rule that outlier are at a distence of at least 3 std from
# The mean
#Create the difference vector of the verible 'Fare' from it's mean.
z_score = (df["Fare"] - df["Fare"].mean()) / df["Fare"].std()
#Cheack which  values are in a distence bigger then 3 [STD] from the mean.

outliers = abs(z_score) > 3
print("Number of outliers  = ",sum(outliers))

print("Minmum of Fare[outliers]  = ",min(df.Fare[outliers]))
#10:38
df.Fare[outliers] = np.nan