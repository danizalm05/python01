"""
59 data_analysis_using_Pandas_Intro_data_loading.py
 -----------------------------------------------------

https://www.youtube.com/watch?v=qy5b2RCdW9o&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=60
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial59_data_analysis_using_Pandas_Intro_data_loading.py  

Think of Pandas as an extension of Numpy where it makes handling of arrays
easy, almost like Excel.

 LOADING, VIEWING AND  UNDERSTANGING DATA


Once you get the csv file, ploting and analyzing is very 
easy with Pandas library. 
Here, just 3 lines to get our plot. 

data file url
https://github.com/bnsreenu/python_for_microscopists/blob/master/other_files/cell_measurements.csv
 
2:30
"""
 
import pandas as pd
 

df = pd.read_csv('data/cell_measurements.csv')
print(df.head())
print(df.columns)
df['Area'].plot(kind='hist', title='Area', bins=50)