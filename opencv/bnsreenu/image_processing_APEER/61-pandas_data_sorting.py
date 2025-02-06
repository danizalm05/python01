"""
61_data_analysis_using_Pandas_data_sorting.py
 -----------------------------------------------------
https://www.youtube.com/watch?v=Kn_Gl12GWq0&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=62
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial61_data_analysis_using_Pandas_data_sorting.py
data file url
https://github.com/bnsreenu/python_for_microscopists/blob/master/other_files/cell_measurements.csv
 

"""    
 
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('data/manual_vs_auto_updated.csv')
print(df.head())
print("\n\n\ndf.columns = ",df.columns)

#Let us sort and assign this to a diferent variable
df2=df.sort_values('Manual', ascending=True)
#We can select just a subset of data, for example to only get Manual column
print(df2['Manual'])

#To get multiple columns, it is just

title_list = ['Manual', 'Auto_th_2']
print(   df[ title_list ] )

#To select subset of rows
print(df[20:30])  #Extracts rows 20 to 30, not including 30.

#Combining above two, to get specific columns from specific rows.
rows =  list(range(20,30))
colums = ['Manual', 'Auto_th_2']
#04:26
print(df.loc[rows,colums]) #    print(df.loc[20:30, ['Manual', 'Auto_th_2']])