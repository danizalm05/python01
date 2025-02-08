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

#Selecting rows using row values, for example if we only want Set 2 info
#Similar to dropping rows we saw earlier.
dfset2 = df['Unnamed: 0'] == 'Set2'
set2_df = df[dfset2]   #    df[df['Unnamed: 0'] == 'Set2']
print(set2_df.tail())
print("\n\nmax(df['Manual']) = ", max(df['Manual']))

#Instead of selection we can do data filtering,
#e.g. filter all values greater than certain size
#Prints True or False.
print("\n\n df['Manual'] > 100 = ",df['Manual'] > 100.)  
#If we want to extract all data with this condition then use square brackets.
print(df[df['Manual'] > 100.])

#We can give multiple conditions to filter
dfmu = df[(df['Manual'] > 80.) & (df['Auto_th_2'] < 60.)]
print("\n\n df[(df['Manual'] > 80.) & (df['Auto_th_2'] <60.)] ")
print("=================================================== ")


print(dfmu)


#We can use for loop to iterate just like we do for lists.
#Let's iterate through Auto, add them and divide by 3 to get 
#averageand compare with Manual value.
for index, row in df.iterrows():
    print("\nindex =", index)#,"\n-----row -----\n", row)
    average_auto = (row['Auto_th_2'] + row['Auto_th_3'] + row['Auto_th_4'])/3
    print("avg = ",round(average_auto),"  Manual = ", row['Manual'])  #ROunding to INT for easy comparison

