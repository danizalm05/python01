"""
63 dealing with null data_in_Pandas
 -----------------------------------------------------
https://www.youtube.com/watch?v=oOJynaTGMvk&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=64
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial63_dealing%20with%20null%20data_in_Pandas.py


data file url
https://github.com/bnsreenu/python_for_microscopists/blob/master/other_files/cell_measurements.csv
 

"""    
 
import pandas as pd
import matplotlib.pyplot as plt 

csv_name = 'data/manual_vs_auto_updated.csv'

df = pd.read_csv(csv_name)
print("\n    ", csv_name,"\n    ==============================")
print(df.head())
 
print(df.isnull())#Shows whether a cell is null or not, not that helpful.

#Drop the entire column, if it makes sense
df = df.drop("Manual2", axis=1)
numOfNan = df.isnull().sum()
print("Num of nulls in a column\n=====\n",numOfNan)   #Shows number of nulls in each column. 

#If we only have handful of rows of null we can afford to drop 
#these rows.
df2 = df.dropna()  #Drops all rows with at least one null value. 
#We can overwrite original df by equating it to df instead of df2.
#Or adding inplace=True inside


print("\n Drops all rows with at least one null value \n    ==============================")

print(df2.head(25))  #See if null rows are gone.e.g. row 12

#If we have a lot of missing data then removing rows or columns
#may not be preferable.
#In such cases data scientists use Imputation technique.
#Just a fancy way of saying, fill it with whatever value
#A good guess would be filling missing values by the mean of the dataset.


print(df['Manual'].describe())  
#Mean value of this column is 100.



df['Manual'].fillna(100, inplace=True)

print('----df.head(25)---------')  
print(df.head(25))   #Notice last entry in MinIntensity filled with 159.8
print('-------------') 
print(df['Manual'].describe())  


#In this example a better way to fill NaN is by filling with 
#average of all auto columns from same row
 
import numpy as np

df = pd.read_csv(csv_name)

df['Manual'] =  df.apply(lambda row: (round((row['Auto_th_2']+row['Auto_th_3']+row['Auto_th_3'])/3)) if np.isnan(row['Manual']) else row['Manual'], axis=1)
print(df.head(25))