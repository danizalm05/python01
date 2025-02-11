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