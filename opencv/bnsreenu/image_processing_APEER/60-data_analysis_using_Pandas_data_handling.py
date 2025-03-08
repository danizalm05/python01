"""
60_data_analysis_using_Pandas_data_handling.py
 -----------------------------------------------------

https://www.youtube.com/watch?v=H2fL7e6baGw&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=61
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial60_data_analysis_using_Pandas_data_handling.py
 

data file url
https://github.com/bnsreenu/python_for_microscopists/blob/master/other_files/cell_measurements.csv
 
Data handling: Deleting Rows and COlumns
 Deleting columns
 Delete Manual2 column
import pandas as pd
df = pd.read_csv('data/manual_vs_auto.csv')

"""
 
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('data/manual_vs_auto_updated.csv')
print(df.head())
print("\ndf.columns = ",df.columns)

df1 = df.drop("Manual2", axis=1) #Creating a new dataframe df1. 
# Axis=1 means referring to column. 
print("\ndf.columns\n------------\n",df.columns)
print("\ndf1.columns after droping Manual2\n------------\n",df1.columns)
 
#To drop multiple columns
df2=df.drop(["Manual2", "Auto_th_2", "Auto_th_3"], axis=1)
 
print("\ndf1.columns after droping Auto_th_2 Auto_th_3\n------------\n",df2.columns)
 

#Inserting new columns, 

df = pd.read_csv('data/manual_vs_auto_updated.csv')
#as easy as just typing...
df['Date'] = "2019-05-06" 

 #New column addded

print("\ndf.head() New column addded\n------------\n",df.head())
#But if you look at the data type....
print("df.dtypes = ",df.dtypes)  #Date is not in date format, it is as object,
          # otherwise string

#To properly format it as date so you can plot it later....
df['Date'] = pd.to_datetime("2019-05-06")

#print(df.head())
print(df.dtypes)


#You can write the data back to a new csv.
#df.to_csv('data/maual_vs_auto_updated.csv') #Open csv file to see


##################
#Deleting rows
 
df = pd.read_csv('data/manual_vs_auto_updated.csv')

#Delete a specific row
df1 = df.drop(df.index[1])
#Delete first 10 rows

print("\nDelete first row \n-----",df1.head())
df = df.iloc[10:,]
print("\nDelete first 10 rows \n-----",df.head())



#Drop all rows if the row value is equal to some string or number
drp= df["Unnamed: 0"] != "Set1"#two values True False
df1 = df[drp]
print(df1.head())