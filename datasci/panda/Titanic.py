#!/usr/bin/env python3
'''
                   titanic
1. taking care of missing data
https://courses.campus.gov.il/courses/course-v1:HIT+ACD_RFP4_DataScienceIntro_HE+2022_1/courseware/0f960b9a58644ff4b9c375b0624f8d18/bd2abf63e2d64ccda87e6371cca3da55/
2. taking care of data duplication
https://courses.campus.gov.il/courses/course-v1:HIT+ACD_RFP4_DataScienceIntro_HE+2022_1/courseware/0f960b9a58644ff4b9c375b0624f8d18/dd409f280fa04f6b8cb552f715d0a0c4/?child=last

https://labs.vocareum.com/main/main.php?m=editor&asnid=537348&stepid=537349&hideNavBar=1

'''


import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt


df = pd.read_csv('./data/titanic.csv', header=0, sep=',')
print(df.head())
print(" \n====df.columns====\n")
print(df.columns,"\n==== end  columns====\n")
print("\n\ndf.info() \n==============\n\n")
print(df.info())
print(" \n== end info ====\n\n")
print(" \ndf.shape\n==================\n",df.shape)




print(" \ndf.dtypes\n==================\n",df.dtypes)
print(" \n== end df.dtypes ====\n\n")

print(" \ndf.describe(include='all'))\n==================\n",df.describe(include='all'))
print(" \n== end df.describe(include='all')) ====\n\n")


#Scan 5 first line of 'Cabin' and print 'True' for   null False for 'non null'
print(" \ndf.Cabin.head().isnull()\n==================\n",df.Cabin.head().isnull())
print(" \n== end df.Cabin.head().isnull() ====\n\n")

#Find number of missing values in 'Cabin'
print(" \ndf.Cabin.isnull().sum()\n==================\n",df.Cabin.isnull().sum())
print(" \n== end df.Cabin.isnull().sum() ====\n\n")


#Copy first 8 lines from the  table
df2 = df.iloc[:8].copy()
print("df2.shape(df.iloc[:8].copy()) = ",df2.shape,'\n\n\n' ,df2)

# drop  lines (axis=0) with 'null' value. if  (axis=1) any cloumn with 'null' will be droped

print("df2.shape(df.iloc[:8].copy()) = ",df2.dropna(axis=0).shape,'\n\n\n' ,df2.dropna(axis=0))
df2 = df.iloc[:8].copy()
df2.dropna(axis=0, how='all')
# drop  lines (axis=0) only if all the values are 'null' value. if  (axis=1) any cloumn
print(df2.dropna(axis=0, how='all'))

df2 = df.iloc[:8].copy()

# drop  lines (axis=0) only if the number  of non 'null' is  then higher from 11 (thresh=11)
print(df2.dropna(axis=0, thresh=11).shape)


df2_clean = df2.dropna(axis=0, thresh=11).copy()#This is a real copy not a referance
df2 = df2.dropna(axis=0, thresh=11) # Change the original 'df'
# we can achieve the same with df2.dropna(axis=0, thresh=11, inplace = True)

df2 = df.iloc[:8].copy()
print("df2.Age.isnull().sum() =   ",df2.Age.isnull().sum())

new_age = df2.Age.fillna(0)# Replace NaN withe 0
print("df2.Age.fillna(0)  = ",new_age)

new_age = df2.Age.fillna(df2.Age.mean())## Replace NaN withe 'mean'
print("\n\ndf.Embarked.describe() = \n-*--------*********-\n",df.Embarked.describe())

dfe= df["Embarked"].fillna('S',inplace=True)# put 's' in NaN vales
print(dfe)
#df.Embarked = df.Embarked.fillna(df.Embarked.mode()[0])

df2.fillna(method = 'ffill')# Fill with close values 'forward fill'
#bfill=  backward fill
print("df.Embarked.duplicated().sum() = ",df.Embarked.duplicated().sum())
# In the 'Embarked' column there only 3 possible values so there are
# many  duplication in the  above output

print("possible values of  Embarked column =", df.Embarked.unique())